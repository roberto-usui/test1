from typing import List
import random

from app.models import Property, Player


class GameService:
    def __init__(self, properties: List[Property], players: List[Player]) -> Player:
        self.properties_hash = {}
        for i in range(len(properties)-1):
            self.properties_hash[i] = properties[i]
        self.players_hash = {}
        for player in players:
            player.total_sum = 300
            self.players_hash[player.id] = player

    def run(self):
        total_turns = 0
        counter = 0
        winner = None
        table_size = len(self.properties_hash)
        while(counter < 1000):
            total_turns += 1
            current_round_players = self.players_hash.copy()
            if len(current_round_players) <= 1:
                break
            for key, player in current_round_players.items():
                player.current_position += random.randint(1, 6)
                if player.current_position > table_size:
                    player.current_position = player.current_position - table_size
                    player.total_sum += 100
                self.property_action(player)
                if self.players_hash[key].total_sum < 0:
                    self.remove_from_game(key)
                if len(self.players_hash) <= 1:
                    break


            counter += 1
        if not winner:
            winners = list(current_round_players.values())
            winners.sort(reverse=True, key=(lambda x: x.total_sum))
            winner = winners[0]

        return {
            'winner': winner,
            'turns': total_turns
        }

    def property_action(self, player: Player):
        prop = self.properties_hash[player.current_position - 1]
        owner = list(filter(lambda x: x.id == prop.owner_id, self.players_hash.values()))
        if owner:
            diff = player.total_sum - prop.rent
            owner[0].total_sum += player.total_sum if diff < 0 else prop.rent
            player.total_sum -= prop.rent
            self.players_hash[player.id] = player
            self.players_hash[owner[0].id] = owner[0]
        elif player.will_buy(prop.price, prop.rent):
            player.total_sum -= prop.price
            prop.owner_id = player.id
            self.players_hash[player.id] = player
            self.properties_hash[player.current_position - 1] = prop

    def remove_from_game(self, player_id: str):
        self.players_hash.pop(player_id, None)
        for key, prop in self.properties_hash.items():
            if prop.owner_id == key:
                prop.owner_id = None
                self.properties_hash[key] = prop
