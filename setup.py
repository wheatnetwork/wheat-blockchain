from setuptools import setup

dependencies = [
    "blspy==1.0.5",  # Signature library
    "chiavdf==1.0.2",  # timelord and vdf verification
    "chiabip158==1.0",  # bip158-style wallet filters
    "chiapos==1.0.4",  # proof of space
    "clvm==0.9.7",
    "clvm_rs==0.1.8",
    "clvm_tools==0.4.3",
    "aiohttp==3.7.4",  # HTTP server for full node rpc
    "aiosqlite==0.17.0",  # asyncio wrapper for sqlite, to store blocks
    "bitstring==3.1.7",  # Binary data management library
    "colorlog==5.0.1",  # Adds color to logs
    "concurrent-log-handler==0.9.19",  # Concurrently log and rotate logs
    "cryptography==3.4.7",  # Python cryptography library for TLS - keyring conflict
    "keyring==23.0.1",  # Store keys in MacOS Keychain, Windows Credential Locker
    "keyrings.cryptfile==1.3.4",  # Secure storage for keys on Linux (Will be replaced)
    #  "keyrings.cryptfile==1.3.8",  # Secure storage for keys on Linux (Will be replaced)
    #  See https://github.com/frispete/keyrings.cryptfile/issues/15
    "PyYAML==5.4.1",  # Used for config file format
    "setproctitle==1.2.2",  # Gives the wheat processes readable names
    "sortedcontainers==2.3.0",  # For maintaining sorted mempools
    "websockets==8.1.0",  # For use in wallet RPC and electron UI
    "click==8.0.1",  # For the CLI
    "dnspython==2.1.0",  # Query DNS seeds
]

upnp_dependencies = [
    "miniupnpc==2.2.2",  # Allows users to open ports on their router
]

dev_dependencies = [
    "pytest",
    "pytest-asyncio",
    "flake8",
    "mypy",
    "black",
    "aiohttp_cors",  # For blackd
    "ipython",  # For asyncio debugging
]

kwargs = dict(
    name="wheat-blockchain",
    author="admin",
    author_email="admin@wheat.network",
    description="Wheat blockchain full node, farmer, timelord, and wallet.",
    url="https://wheat.network/",
    license="Apache License",
    python_requires=">=3.7, <4",
    keywords="wheat blockchain node",
    install_requires=dependencies,
    setup_requires=["setuptools_scm"],
    extras_require=dict(
        uvloop=["uvloop"],
        dev=dev_dependencies,
        upnp=upnp_dependencies,
    ),
    packages=[
        "build_scripts",
        "wheat",
        "wheat.cmds",
        "wheat.clvm",
        "wheat.consensus",
        "wheat.daemon",
        "wheat.full_node",
        "wheat.timelord",
        "wheat.farmer",
        "wheat.harvester",
        "wheat.introducer",
        "wheat.plotting",
        "wheat.pools",
        "wheat.protocols",
        "wheat.rpc",
        "wheat.server",
        "wheat.simulator",
        "wheat.types.blockchain_format",
        "wheat.types",
        "wheat.util",
        "wheat.wallet",
        "wheat.wallet.puzzles",
        "wheat.wallet.rl_wallet",
        "wheat.wallet.cc_wallet",
        "wheat.wallet.did_wallet",
        "wheat.wallet.settings",
        "wheat.wallet.trading",
        "wheat.wallet.util",
        "wheat.ssl",
        "mozilla-ca",
    ],
    entry_points={
        "console_scripts": [
            "wheat = wheat.cmds.wheat:main",
            "wheat_wallet = wheat.server.start_wallet:main",
            "wheat_full_node = wheat.server.start_full_node:main",
            "wheat_harvester = wheat.server.start_harvester:main",
            "wheat_farmer = wheat.server.start_farmer:main",
            "wheat_introducer = wheat.server.start_introducer:main",
            "wheat_timelord = wheat.server.start_timelord:main",
            "wheat_timelord_launcher = wheat.timelord.timelord_launcher:main",
            "wheat_full_node_simulator = wheat.simulator.start_simulator:main",
        ]
    },
    package_data={
        "wheat": ["pyinstaller.spec"],
        "wheat.wallet.puzzles": ["*.clvm", "*.clvm.hex"],
        "wheat.util": ["initial-*.yaml", "english.txt"],
        "wheat.ssl": ["wheat_ca.crt", "wheat_ca.key", "dst_root_ca.pem"],
        "mozilla-ca": ["cacert.pem"],
    },
    use_scm_version={"fallback_version": "unknown-no-.git-directory"},
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    zip_safe=False,
)


if __name__ == "__main__":
    setup(**kwargs)
