# === CODE PYTHON EXACT DU PSEUDO-CODE ===

def ELECT_DELEGATES(U, C, K) :
    # score[c] ← 0 for all c in C
    score = {}
    for c in C:
        score[c] = 0
    
    # for each voter uj:
    for uj in U:
        # chosen ← uj.vote_set ⊆ C
        chosen = uj['vote_set']
        
        # for each candidate c in chosen:
        for c in chosen:
            if c in C:
                # score[c] ← score[c] + w[j]
                score[c] = score[c] + uj['w']
    
    # D ← top-K candidates by score
    # Trier par score décroissant et prendre K premiers
    sorted_candidates = sorted(score.items(), key=lambda x: x[1], reverse=True)
    D = [candidate for candidate, _ in sorted_candidates[:K]]
    
    return D


def PRODUCE_BLOCKS(D):

    # schedule ← ROUND_ROBIN_ORDER(D)
    schedule = D  # Ordre round-robin simple
    K = len(D)
    
    # for each slot t:
    for t in range(K * 2):  # Simuler 2 tours complets
        # producer ← schedule[t mod K]
        producer = schedule[t % K]
        
        # block ← BUILD_BLOCK(mempool)
        block = {
            'slot': t,
            'producer': producer,
            'data': f"Block at slot {t}"
        }
        
        # SIGN(block, producer.private_key) - simulé
        block['signature'] = f"signed_by_{producer}"
        
        # BROADCAST(block) - simulé
        print(f"Slot {t}: {producer} produced block")
        
    return


def GOVERNANCE_UPDATE(U, C, K):

    # D ← ELECT_DELEGATES(U, C, K)
    D = ELECT_DELEGATES(U, C, K)
    
    # update schedule accordingly
    print(f"New delegates after governance update: {D}")
    return D
