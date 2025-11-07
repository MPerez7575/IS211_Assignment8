import argparse
from piggame.factory import PlayerFactory
from piggame.game import Game
from piggame.timed_proxy import TimedGameProxy

def parse_args():
    parser = argparse.ArgumentParser(description="Pig Dice Game with Design Patterns")
    parser.add_argument("--player1", choices=["human", "computer"], default="human")
    parser.add_argument("--player2", choices=["human", "computer"], default="computer")
    parser.add_argument("--timed", action="store_true", help="Enable 60-second time limit")
    parser.add_argument("--seed", type=int, default=None, help="Random seed for die rolls")
    return parser.parse_args()

def main():
    args = parse_args()
    p1 = PlayerFactory.create(args.player1, "Player 1")
    p2 = PlayerFactory.create(args.player2, "Player 2")

    game = Game(p1, p2, seed=args.seed)
    if args.timed:
        game = TimedGameProxy(game)

    winner = game.play()
    print(f"\n🏁 Game Over! Winner: {winner.name} with {winner.score} points.\n")

if __name__ == "__main__":
    main()
