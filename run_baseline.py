from env import MarketEnv
from tasks import ALL_TASKS
from models import Action


def simple_agent(obs):
    if obs.buyer_offer > 0.9 * obs.listed_price:
        return Action(action_type="accept")
    elif obs.buyer_offer > 0.5 * obs.listed_price:
        return Action(action_type="counter")
    else:
        return Action(action_type="reject")


def run():
    total_score = 0

    for task in ALL_TASKS:
        print("\n" + "=" * 40)
        print("Running Task:", task["name"])
        print("=" * 40)

        env = MarketEnv(task)
        obs = env.reset()

       
        print("Buyer Type:", env.buyer_type)

        done = False

        while not done:
            print(f"\nRound {obs.round}")
            print(f"Current Offer: {obs.buyer_offer}")

            action = simple_agent(obs)
            print(f"Agent Action: {action.action_type}")

            obs, reward, done, _ = env.step(action)

        print("Final Reward:", reward.score)
        total_score += reward.score

    print("\nTOTAL SCORE:", total_score)


if __name__ == "__main__":
    run()