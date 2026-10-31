"""Pure stable-distribution model; no recognition, motor control, or hardware claims.

Occurrence IDs below are simulation ground truth. Hardware must reconcile its
observed sequence before executing a plan; recognition cannot supply physical IDs.
"""

from collections import Counter
from dataclasses import dataclass
from math import ceil
from random import Random


def passes_for_groups(groups: int, radix: int) -> int:
    if groups < 0 or radix < 2:
        raise ValueError("groups must be nonnegative and radix at least two")
    passes, labels = 0, 1
    while labels < groups:
        labels *= radix
        passes += 1
    return passes


@dataclass(frozen=True)
class Plan:
    labels: tuple[int, ...]  # indexed by original occurrence ID
    target: tuple[int, ...]
    rising_sequences: int
    passes: int
    radix: int


def plan_order(keys, radix=4) -> Plan:
    """Find minimum passes for the observed order with stable equal-key ties.

    R = 1 + descents in original positions read in target order. Stable passes
    provide at most radix**p lexicographic labels. Each descent requires a label
    boundary; sorting by these sequence labels attains the lower bound.
    """
    keys = tuple(keys)
    target = tuple(sorted(range(len(keys)), key=keys.__getitem__))
    labels = [0] * len(keys)
    group = 0
    for index, occurrence in enumerate(target):
        if index and occurrence < target[index - 1]:
            group += 1
        labels[occurrence] = group
    groups = group + 1 if keys else 0
    return Plan(tuple(labels), target, groups, passes_for_groups(groups, radix), radix)


def partition(order, labels, digit, radix):
    bins = [[] for _ in range(radix)]
    for occurrence in order:
        bins[(labels[occurrence] // radix**digit) % radix].append(occurrence)
    return bins


def apply_plan(plan, order=None):
    current = list(range(len(plan.labels))) if order is None else list(order)
    for digit in range(plan.passes):
        current = [item for bucket in partition(current, plan.labels, digit, plan.radix)
                   for item in bucket]
    return current


def group_recursion_work(n, radix):
    """Ideal balanced recursive distribution to singleton leaves, as in review."""
    if n < 0 or radix < 2:
        raise ValueError("invalid count or radix")
    loads = cycles = 0
    pending = [n]
    while pending:
        size = pending.pop()
        if size <= 1:
            continue
        loads += 1
        cycles += size
        quotient, remainder = divmod(size, radix)
        pending.extend(quotient + (i < remainder) for i in range(radix))
    return loads, cycles


def cassette_chunks(bins, capacity):
    """Chronological chunks per route. Concatenate routes, then their chunks."""
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    return [[bucket[i:i + capacity] for i in range(0, len(bucket), capacity)]
            for bucket in bins]


def sequence_matches(expected_keys, observed_keys):
    """Compare order AND multiplicity; assumes recognized keys themselves are true."""
    return tuple(expected_keys) == tuple(observed_keys)


def workload(keys, radix, capacity=200):
    """Include one inventory pass, then planned passes; explicit cassette chunks.

    Chunks and mid-route replacements are NOT visits: visits may combine actions.
    This model assumes FIFO-equivalent handling and a reliable pause before spill.
    """
    keys = tuple(keys)
    if capacity <= 0:
        raise ValueError("capacity must be positive")
    plan = plan_order(keys, radix)
    current = list(range(len(keys)))
    scan_chunks = ceil(len(keys) / capacity)
    chunks = scan_chunks
    input_loads = scan_chunks
    next_input_chunks = scan_chunks
    replacements = max(0, scan_chunks - 1)
    for digit in range(plan.passes):
        input_loads += next_input_chunks
        bins = partition(current, plan.labels, digit, radix)
        routed_chunks = cassette_chunks(bins, capacity)
        next_input_chunks = sum(len(parts) for parts in routed_chunks)
        chunks += next_input_chunks
        replacements += sum(max(0, len(parts) - 1) for parts in routed_chunks)
        current = [item for parts in routed_chunks for chunk in parts for item in chunk]
    assert tuple(current) == plan.target
    assert Counter(current) == Counter(range(len(keys)))
    return {
        "runs": plan.rising_sequences,
        "planned_passes_including_scan": (1 + plan.passes) if keys else 0,
        "dense_rank_passes_including_scan":
            (1 + passes_for_groups(len(set(keys)), radix)) if keys else 0,
        "card_cycles": len(keys) * (1 + plan.passes),
        "output_chunks_including_scan": chunks,
        "input_chunk_loads": input_loads,
        "mid_route_replacements": replacements,
    }


def main():
    rng = Random(1)
    examples = []
    for count in (1000, 5000):
        values = list(range(count))
        rng.shuffle(values)
        examples.append((f"random-{count}", values))
    newcomers = set(rng.sample(range(2100), 100))
    merged = [v for v in range(2100) if v not in newcomers]
    merged += rng.sample(sorted(newcomers), 100)
    examples.append(("sorted-2000-plus-100", merged))
    examples.append(("already-sorted-1000", list(range(1000))))
    examples.append(("reversed-1000", list(reversed(range(1000)))))
    for name, keys in examples:
        for radix in (4, 8):
            stats = workload(keys, radix)
            recursive_loads, recursive_cycles = group_recursion_work(len(keys), radix)
            print(f"{name} k={radix}: {stats}; "
                  f"catalog100k={passes_for_groups(100000, radix)}; "
                  f"recursive_loads={recursive_loads} recursive_cycles={recursive_cycles}")


if __name__ == "__main__":
    main()
