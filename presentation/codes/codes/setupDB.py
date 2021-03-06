...
'settings',
(
    'id INTEGER PRIMARY KEY AUTOINCREMENT',
    'market_id INT',
    'nickname TEXT',
    'namecoin_id TEXT',
    'secret TEXT',
    'sin TEXT',
    'pubkey TEXT',
    'guid TEXT',
    'email TEXT',
    'PGPPubKey TEXT',
    'PGPPubkeyFingerprint TEXT',
    'bcAddress TEXT',
    'bitmessage TEXT',
    'storeDescription TEXT',
    'street1 TEXT',
    'street2 TEXT',
    'city TEXT',
    'stateRegion TEXT',
    'stateProvinceRegion TEXT',
    'zip TEXT',
    'country TEXT',
    'countryCode TEXT',
    'welcome TEXT',
    'recipient_name TEXT',
    'arbiter BOOLEAN',
    'arbiterDescription TEXT',
    'trustedArbiters TEXT',
    'privkey TEXT',
    'obelisk TEXT',
    'notaries TEXT',
    'notary BOOLEAN',
    'FOREIGN KEY(market_id) REFERENCES markets(id)'
)
...
