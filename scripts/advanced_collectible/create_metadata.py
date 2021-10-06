from brownie import AdvancedCollectible, network

def main():
    print("working on " + network.show_active())
    advanced_collectible = AdvancedCollectible[len(AdvancedCollectible) -1]
    number_of_tokens = advanced_collectible.tokenCounter()
    print(number_of_tokens)
