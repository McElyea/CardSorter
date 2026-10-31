"""Checks of ordering, finite-capacity handling, and reload-error assumptions."""

from collections import deque
from itertools import permutations, product
from random import Random
import unittest

from software.sort_model import (
    apply_plan, cassette_chunks, group_recursion_work, partition,
    passes_for_groups, plan_order, sequence_matches, workload,
)


class SortModelTests(unittest.TestCase):
    def test_all_permutations_through_seven(self):
        for count in range(8):
            for keys in permutations(range(count)):
                for radix in (2, 4, 8):
                    plan = plan_order(keys, radix)
                    result = apply_plan(plan)
                    self.assertEqual(tuple(result), plan.target)
                    self.assertEqual([keys[i] for i in result], sorted(keys))

    def test_duplicate_keys_preserve_stable_ties(self):
        for count in range(7):
            for keys in product(range(3), repeat=count):
                plan = plan_order(keys)
                self.assertEqual(tuple(apply_plan(plan)), plan.target)

    def test_minimum_with_independent_breadth_first_oracle(self):
        # Enumerate physical stable binary distributions, without run-count logic.
        for count in range(1, 5):
            goal = tuple(range(count))
            for start in permutations(goal):
                seen = {start}
                pending = deque([(start, 0)])
                while pending:
                    state, distance = pending.popleft()
                    if state == goal:
                        self.assertEqual(plan_order(start, 2).passes, distance)
                        break
                    for routes in product(range(2), repeat=count):
                        following = tuple(value for bin_id in range(2)
                                          for value, route in zip(state, routes)
                                          if route == bin_id)
                        if following not in seen:
                            seen.add(following)
                            pending.append((following, distance + 1))

    def test_integer_boundaries(self):
        self.assertEqual([passes_for_groups(n, 4) for n in (0, 1, 4, 5, 16, 17)],
                         [0, 0, 1, 2, 2, 3])
        with self.assertRaises(ValueError):
            plan_order([0], 1)

    def test_review_group_counts(self):
        self.assertEqual(group_recursion_work(1000, 4), (341, 5000))
        self.assertEqual(group_recursion_work(1000, 8), (561, 3976))

    def test_reproduced_random_job(self):
        keys = list(range(1000))
        Random(1).shuffle(keys)
        for radix, traversals, dense, loads, chunks in ((4, 6, 6, 42, 43), (8, 4, 5, 26, 29)):
            stats = workload(keys, radix, 200)
            self.assertEqual(stats["runs"], 506)
            self.assertEqual(stats["planned_passes_including_scan"], traversals)
            self.assertEqual(stats["dense_rank_passes_including_scan"], dense)
            self.assertEqual(stats["input_chunk_loads"], loads)
            self.assertEqual(stats["output_chunks_including_scan"], chunks)

    def test_spill_chunks_preserve_logical_bin_order(self):
        keys = list(reversed(range(301)))
        for capacity in (1, 17, 200):
            plan = plan_order(keys)
            order = list(range(len(keys)))
            for digit in range(plan.passes):
                bins = partition(order, plan.labels, digit, plan.radix)
                chunks = cassette_chunks(bins, capacity)
                self.assertTrue(all(len(chunk) <= capacity for parts in chunks for chunk in parts))
                order = [item for parts in chunks for chunk in parts for item in chunk]
            self.assertEqual(tuple(order), plan.target)

    def test_one_route_can_overflow_before_hopper_is_empty(self):
        parts = cassette_chunks([list(range(201)), [], [], []], 200)
        self.assertEqual([len(p) for p in parts[0]], [200, 1])

    def test_reidentification_does_not_repair_old_plan(self):
        keys = [0, 2, 1, 3]
        plan = plan_order(keys, 4)
        reversed_occurrences = list(reversed(range(len(keys))))
        observed = [keys[i] for i in reversed_occurrences]
        self.assertFalse(sequence_matches(keys, observed))
        self.assertNotEqual([keys[i] for i in apply_plan(plan, reversed_occurrences)], sorted(keys))
        new_plan = plan_order(observed, 4)
        self.assertEqual([observed[i] for i in apply_plan(new_plan)], sorted(keys))

    def test_mid_pass_reject_leaves_remainder_sorted(self):
        # Divert one occurrence at any point in any pass; the rest still finish ordered.
        for keys in ([5, 3, 0, 4, 1, 2, 3], list(reversed(range(9)))):
            plan = plan_order(keys, 2)
            for reject_pass in range(plan.passes):
                for rejected in range(len(keys)):
                    order = list(range(len(keys)))
                    for digit in range(plan.passes):
                        if digit == reject_pass:
                            order.remove(rejected)
                        order = [item for bucket in partition(order, plan.labels, digit, plan.radix)
                                 for item in bucket]
                    expected = [item for item in plan.target if item != rejected]
                    self.assertEqual(order, expected)

    def test_reconciliation_checks_counts_and_order(self):
        self.assertTrue(sequence_matches([0, 0, 1], [0, 0, 1]))
        self.assertFalse(sequence_matches([0, 0, 1], [0, 1, 0]))
        self.assertFalse(sequence_matches([0, 0, 1], [0, 1]))

    def test_runs_are_inverse_descents_not_adjacent_runs(self):
        self.assertEqual(plan_order([0, 2, 4, 1, 3, 5]).rising_sequences, 3)

    def test_scan_and_capacity_accounting(self):
        self.assertEqual(workload([], 4)["planned_passes_including_scan"], 0)
        stats = workload(list(range(1000)), 4, 200)
        self.assertEqual(stats["planned_passes_including_scan"], 1)
        self.assertEqual(stats["output_chunks_including_scan"], 5)
        self.assertEqual(stats["mid_route_replacements"], 4)
        # Carry partly filled output cassettes forward without repacking cards.
        stats = workload([3, 2, 1, 0], 2, 3)
        self.assertEqual(stats["input_chunk_loads"], 6)


if __name__ == "__main__":
    unittest.main()
