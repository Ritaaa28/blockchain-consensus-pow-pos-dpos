import random

# === PSEUDO-CODE ===
# procedure SELECT_PROPOSER(V, r):
#     total ← sum_i s[i]
#     u ← UNIFORM(0, total) using r
#     running ← 0
#     for each validator vi:
#         running ← running + s[i]
#         if running ≥ u:
#             return vi

def SELECT_PROPOSER(validators, seed=None):
    """
    Input: validators = [{'name': 'Alice', 'stake': 100}, ...], seed
    Output: Le validateur sélectionné proportionnellement à son stake
    """
    if seed is not None:
        random.seed(seed)
    
    # total ← sum_i s[i]
    total_stake = sum(v['stake'] for v in validators)
    
    # u ← UNIFORM(0, total) using r
    target = random.uniform(0, total_stake)
    
    # running ← 0
    running_sum = 0
    
    # for each validator vi:
    for validator in validators:
        # running ← running + s[i]
        running_sum += validator['stake']
        
        # if running ≥ u:
        if running_sum >= target:
            # return vi
            return validator
    
    return validators[-1]  # Fallback (théoriquement jamais atteint)

