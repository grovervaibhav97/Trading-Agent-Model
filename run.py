from environment import TradingEnvironment
from agent import TradingAgent

env = TradingEnvironment("data.csv")
agent = TradingAgent()

state = env.reset()

while True:
    action = agent.act()
    state, reward, done = env.step(action)
    print("Price:", state, "Net Worth:", reward)
    if done:
        break
