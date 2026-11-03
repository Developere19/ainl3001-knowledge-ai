"""AINL3001 — Topic 7: Knowledge Representation and Logical Reasoning.

Student starter: complete the TODOs in Tasks 3 and 4.
This lab uses propositional facts and simple IF/THEN rules.

BSP
2026
"""

# TASK 1 — Represent facts (provided; inspect and experiment).
facts = {"rainy", "weekday"}

# TASK 2 — Represent rules (provided; inspect and experiment).
# Each rule is (list_of_required_facts, conclusion).
# All conditions must be known before the conclusion can be inferred.
rules = [
    (["rainy"], "take_umbrella"),
    (["rainy", "cold"], "wear_coat"),
    (["take_umbrella"], "stay_dry"),
]


def forward_chaining(known_facts, rules):
    #Return all original and inferred facts without changing known_facts.

    #TASK 3:
    #1. Copy known_facts into a new set.
    inferred_facts = set(known_facts)

    while True:
        new_fact_added = False

    #2. Examine every rule and add its conclusion when ALL conditions hold.
        for conditions, conclusion in rules:
            # Check whether ALL conditions are already known
            if all(condition in inferred_facts for condition in conditions):

                # Only add the conclusion if it is new
                if conclusion not in inferred_facts:
                    inferred_facts.add(conclusion)
                    new_fact_added = True

    #3. Repeat until an entire pass adds no new facts.
        if not new_fact_added:
            break
    #4. Return the completed set.
    return inferred_facts
    
    


def query(inferred_facts, statement):
    """TASK 4 — Return True if statement is established in inferred_facts.

    A False result means 'not established', not necessarily 'false'.
    """
    return statement in inferred_facts


if __name__ == "__main__":
    print("=" * 55)
    print("TASK 0 — MANUAL REASONING")
    print("=" * 55)



    print("Initial facts:", sorted(facts))
    print("Rules:")
    for conditions, conclusion in rules:
        print(f"  IF {' AND '.join(conditions)} THEN {conclusion}")
    print("\nBefore coding, predict whether these can be inferred:")
    print("  take_umbrella?  stay_dry?  wear_coat?  Why?")

    print("\n" + "=" * 55)
    print("TASKS 3–4 — FORWARD CHAINING AND QUERIES")
    print("=" * 55)
    inferred = forward_chaining(facts, rules)
    if inferred is None:
        print("Complete forward_chaining() to see inferred knowledge.")
    else:
        print("Initial facts:", sorted(facts))
        print("All known facts:", sorted(inferred))
        for statement in ("take_umbrella", "stay_dry", "wear_coat"):
            print(f"Can infer {statement}? {query(inferred, statement)}")

    print("\nTASK 5 — BACKWARD CHAINING (discussion)")
    print("Goal: stay_dry. Which rule concludes it? What must be true first?")

    print("1. Which rule has stay_dry as its conclusion?")
    print("The rule IF take_umbrella THEN stay_dry.\n")

    print("2. What condition does that rule require?")
    print("It requires take_umbrella to be true.\n")

    print("3. Which rule could establish that condition?")
    print("The rule IF rainy THEN take_umbrella can establish take_umbrella.\n")

    print("4. Does the chain ultimately reach an initial fact?")
    print("Yes. The chain reaches rainy, which is already an initial fact.\n")

    print("Backward chain: stay_dry <- take_umbrella <- rainy")

    print("\nTASK 6 — LOGIC DISCUSSION")
    print("Is 'IF rainy THEN take_umbrella' always true in the real world?")
    print("What assumptions does the rule make?")

    print("1. Does the rule IF rainy THEN take_umbrella have to be true in the real world?")
    print("No. It is a rule that we have chosen to accept inside this knowledge base. In the real world, someone may choose not to take an umbrella even when it is raining.\n")

    print("2. What assumptions are we making when we include this rule in the knowledge base?")
    print("We are assuming that whenever rainy is known to be true, take_umbrella should also be treated as true according to the rules of our model.\n")

    print("3. How is logical inference different from statistical reasoning under uncertainty?")
    print("Logical inference derives a conclusion when the required facts and rules are satisfied. Statistical reasoning instead deals with probabilities and uncertainty, where a conclusion may be likely without being guaranteed.\n")


    print("\nREFLECTION QUESTIONS")

    print("1. What is logical entailment?")
    print("Logical entailment means that a conclusion must be true whenever the facts and rules in the knowledge base are true.\n")

    print("2. How does forward chaining work?")
    print("Forward chaining is a data-driven reasoning method. It starts with known facts and repeatedly applies rules to derive new facts until no more conclusions can be inferred.\n")

    print("3. How does backward chaining differ from forward chaining?")
    print("Forward chaining starts with known facts and works towards possible conclusions. Backward chaining is goal-driven: it starts with a goal and works backwards to determine what facts must be true to prove that goal.\n")

    print("4. What are the limitations of propositional logic?")
    print("Propositional logic treats each statement as an indivisible true-or-false proposition. It cannot represent general relationships between many individuals, so many separate statements may be needed.\n")