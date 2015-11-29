...
        self.send_raw(
            json.dumps({
                'type': 'hello',
                'pubkey': self.transport.pubkey,
                'uri': self.transport.uri,
                'senderGUID': self.transport.guid,
                'senderNick': self.transport.nickname,
                'senderNamecoin': self.transport.namecoin_id,
                'v': constants.VERSION
            }),
            cb
        )

...

        # Include sender information and version
        data['guid'] = self.guid
        data['senderGUID'] = self.transport.guid
        data['uri'] = self.transport.uri
        data['pubkey'] = self.transport.pubkey
        data['senderNick'] = self.transport.nickname
        data['senderNamecoin'] = self.transport.namecoin_id
        data['v'] = constants.VERSION
...
