from pathlib import Path
from brownie import chain, project, accounts, Contract, VeYfiRewards, Gauge , ExtraReward ,GaugeFactory, Token, config, Registry

VaultProject = project.load(
    Path.home() / ".brownie" / "packages" / config["dependencies"][0]
)
VaultRegistry = Vault = VaultProject.Registry

Vault = VaultProject.Vault


def main():
    account = accounts.load("testnet_deploy")

    registry = Registry.at("0x4147966617083f42AB5A990372ddB81d3DcF2959")

    # deploy a vault
    vault_registry = VaultRegistry.at("0x56F970b3E6AF228533A8F556E10aD45f5781cF45")

    token = account.deploy(Token, "test token 3")
    
    vault_tx = vault_registry.newVault(token, account, account, "yTest3", "yt3", {"from": account})
    vault = vault_tx.events["NewVault"]["vault"]
    # vault = 
    # # create gauge
    tx = registry.addVaultToRewards(vault, account, account, {"from": account})
    gauge = tx.events["GaugeCreated"]["gauge"]
    print("token: ", token)
    print("vault: ", vault)
    print("gauge: ", gauge)
    