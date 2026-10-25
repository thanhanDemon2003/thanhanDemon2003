<p align="center">
  <img src="./assets/banner.svg" alt="Nguyen Thanh An: software engineer, AI engineer, game developer, AI and math researcher. A horned robot agent with arms and legs rests a hand on its chin beside a reasoning trace that types itself out." width="100%">
</p>

<p align="center">
  <a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=500&size=20&pause=1200&color=3DFFA0&center=true&vCenter=true&width=560&height=36&lines=Reading+papers.+Running+experiments.;Building+agents+that+use+tools;Turning+math+into+working+code;Shipping+backends%2C+models+and+games;Never+done+learning" alt="Reading papers. Running experiments. Building agents that use tools. Turning math into working code. Shipping backends, models and games. Never done learning."></a>
</p>

<p align="center">
  <a href="https://fullstackthinker.com/"><img src="./assets/link-website.svg" height="38" alt="Website"></a>
  <a href="https://www.linkedin.com/in/fullstackthinker26/"><img src="./assets/link-linkedin.svg" height="38" alt="LinkedIn"></a>
  <a href="https://www.upwork.com/freelancers/~01662ddccd4c2b19b1?mp_source=share"><img src="./assets/link-upwork.svg" height="38" alt="Upwork"></a>
  <a href="https://www.facebook.com/thanhanthinker/"><img src="./assets/link-facebook.svg" height="38" alt="Facebook"></a>
  <a href="mailto:devnguyenthanhan26@gmail.com"><img src="./assets/link-email.svg" height="38" alt="Email"></a>
</p>

<p align="center">
  <img src="./assets/divider.svg" width="100%" alt="">
</p>

## Meet thinker

Friends call me *thinker*. I think on paper before I type, then let the work loop: observe, reason, plan, act, reflect. Inside my head it looks like one orchestrator and a small team of specialist agents.

<p align="center">
  <img src="./assets/agents.svg" alt="Thinker, the orchestrator, takes a request, sends tasks to a software agent, an AI agent, a game agent and a math agent, then merges their results and writes notes" width="100%">
</p>

## Four ways I work

<p align="center">
  <img src="./assets/roles.svg" alt="Software engineering, AI engineering, game development, AI and math research" width="100%">
</p>

One engineer, four disciplines. Each one sharpens the others: systems thinking for models, optimization for games, and math for all of it.

## About me

```python
class Thinker:
    name = "Nguyen Thanh An"
    alias = "thinker"
    roles = [
        "software engineer",
        "AI engineer",
        "game developer",
        "AI & math researcher",
    ]
    site = "fullstackthinker.com"
    mindset = "always a student of the problem"

    def run(self) -> None:
        while True:
            problem = self.observe()          # find a problem worth solving
            insight = self.reason(problem)    # derive it on paper first
            plan = self.plan(insight)         # backend + model + game loop
            result = self.act(plan)           # write it, ship it
            self.reflect(result)              # what broke? what did I learn?
            # "I always try my best!"

    def delegate(self, goal: str):
        # my stand-in agent: plans, picks a tool, reads the result, remembers it
        return DemonAgent(tools=["api", "model", "game", "math"]).run(goal)
```

## Always learning

<p align="center">
  <img src="./assets/learning.svg" alt="How I learn: read, derive, build, break, write, repeat. A loss curve that falls but never reaches zero." width="100%">
</p>

What I am digging into right now:

<!-- EDIT: replace these rows with what you are really studying this month -->
<table>
  <tr>
    <td width="150"><b>Math</b></td>
    <td>Linear algebra, optimization and probability, worked by hand before any code.</td>
  </tr>
  <tr>
    <td><b>AI</b></td>
    <td>Transformers, fine-tuning and reinforcement learning, reimplemented to understand them.</td>
  </tr>
  <tr>
    <td><b>Agents</b></td>
    <td>Tool use, planning, memory and evals for agents that act on their own.</td>
  </tr>
  <tr>
    <td><b>Games</b></td>
    <td>Procedural generation and learning agents that live inside game worlds.</td>
  </tr>
  <tr>
    <td><b>Software</b></td>
    <td>Distributed systems, and backends designed to fail gracefully.</td>
  </tr>
</table>

<p align="center">
  <img src="./assets/divider.svg" width="100%" alt="">
</p>

## Agents I like to build

<p align="center">
  <img src="./assets/agent.svg" alt="An AI agent loop: a horned robot agent plans, calls one of four tools (API, model, game, math), reads the result and stores it in memory" width="100%">
</p>

The little horned bot is my stand-in for an agent. It plans, picks a tool, reads what comes back and remembers it. Its four tools happen to be my four disciplines.

<p align="center">
  <img src="./assets/agent-trace.svg" alt="An illustrative agent trace typed out line by line: goal, think, tool, observation, correction, lesson saved to memory" width="100%">
</p>

## Notes from my math notebook

Three equations I keep coming back to, re-deriving and re-reading. Each one shows up in more than one of my four disciplines.

**Optimization.** How every model I train learns: step downhill on the loss.

$$\theta_{t+1} = \theta_t - \eta\,\nabla_\theta \mathcal{L}(\theta_t)$$

**Attention.** The core operation inside modern transformers.

$$\mathrm{Attention}(Q,K,V) = \mathrm{softmax}\!\left(\frac{QK^{\top}}{\sqrt{d_k}}\right)V$$

**Value of a state.** The idea behind learning agents and game AI.

$$V^{\pi}(s) = \mathbb{E}_{\pi}\!\left[\sum_{t=0}^{\infty} \gamma^{t}\, r_{t+1} \;\middle|\; s_0 = s\right]$$

## Tech stack

<table>
  <tr>
    <td width="190"><b>Software engineering</b></td>
    <td>
      <img src="https://img.shields.io/badge/-Go-0B1510?style=flat-square&logo=go&logoColor=3DFFA0" alt="Go">
      <img src="https://img.shields.io/badge/-C%23-0B1510?style=flat-square&logo=dotnet&logoColor=3DFFA0" alt="C#">
      <img src="https://img.shields.io/badge/-Node.js-0B1510?style=flat-square&logo=nodedotjs&logoColor=3DFFA0" alt="Node.js">
      <img src="https://img.shields.io/badge/-FastAPI-0B1510?style=flat-square&logo=fastapi&logoColor=3DFFA0" alt="FastAPI">
      <img src="https://img.shields.io/badge/-PostgreSQL-0B1510?style=flat-square&logo=postgresql&logoColor=3DFFA0" alt="PostgreSQL">
      <img src="https://img.shields.io/badge/-Firebase-0B1510?style=flat-square&logo=firebase&logoColor=3DFFA0" alt="Firebase">
      <img src="https://img.shields.io/badge/-AWS-0B1510?style=flat-square" alt="AWS">
      <img src="https://img.shields.io/badge/-Google%20Cloud-0B1510?style=flat-square&logo=googlecloud&logoColor=3DFFA0" alt="Google Cloud">
      <img src="https://img.shields.io/badge/-React%20Native-0B1510?style=flat-square&logo=react&logoColor=3DFFA0" alt="React Native">
      <img src="https://img.shields.io/badge/-Git-0B1510?style=flat-square&logo=git&logoColor=3DFFA0" alt="Git">
    </td>
  </tr>
  <tr>
    <td><b>AI engineering</b></td>
    <td>
      <img src="https://img.shields.io/badge/-Python-0B1510?style=flat-square&logo=python&logoColor=3DFFA0" alt="Python">
      <img src="https://img.shields.io/badge/-PyTorch-0B1510?style=flat-square&logo=pytorch&logoColor=3DFFA0" alt="PyTorch">
      <img src="https://img.shields.io/badge/-TensorFlow-0B1510?style=flat-square&logo=tensorflow&logoColor=3DFFA0" alt="TensorFlow">
      <img src="https://img.shields.io/badge/-Pandas-0B1510?style=flat-square&logo=pandas&logoColor=3DFFA0" alt="Pandas">
      <img src="https://img.shields.io/badge/-OpenAI%20API-0B1510?style=flat-square" alt="OpenAI API">
    </td>
  </tr>
  <tr>
    <td><b>Game development</b></td>
    <td>
      <img src="https://img.shields.io/badge/-Unity-0B1510?style=flat-square&logo=unity&logoColor=3DFFA0" alt="Unity">
      <img src="https://img.shields.io/badge/-Godot-0B1510?style=flat-square&logo=godotengine&logoColor=3DFFA0" alt="Godot">
      <img src="https://img.shields.io/badge/-C%23-0B1510?style=flat-square&logo=dotnet&logoColor=3DFFA0" alt="C#">
    </td>
  </tr>
  <tr>
    <td><b>AI and math research</b></td>
    <td>
      <img src="https://img.shields.io/badge/-NumPy-0B1510?style=flat-square&logo=numpy&logoColor=3DFFA0" alt="NumPy">
      <img src="https://img.shields.io/badge/-SciPy-0B1510?style=flat-square&logo=scipy&logoColor=3DFFA0" alt="SciPy">
      <img src="https://img.shields.io/badge/-Jupyter-0B1510?style=flat-square&logo=jupyter&logoColor=3DFFA0" alt="Jupyter">
      <img src="https://img.shields.io/badge/-LaTeX-0B1510?style=flat-square&logo=latex&logoColor=3DFFA0" alt="LaTeX">
      <img src="https://img.shields.io/badge/-PyTorch-0B1510?style=flat-square&logo=pytorch&logoColor=3DFFA0" alt="PyTorch">
    </td>
  </tr>
</table>

## Activity

<p align="center">
  <img src="./assets/activity.svg" alt="Contribution activity over the last 12 months: total, current streak, longest streak and busiest day" width="100%">
</p>

<p align="center">
  <img src="./assets/stats.svg" alt="Languages used in public repositories, with public repo, star and follower counts" width="100%">
</p>

## Support my work

<p align="center">
  <img src="./imgs/qr.png" width="240" alt="QR code to support Nguyen Thanh An">
</p>

<p align="center">
  If my projects helped you, or you want to back what I build next, a coffee goes a long way.<br>
  Scan the QR code above to buy me one.
</p>

<p align="center">
  <img src="./assets/divider.svg" width="100%" alt="">
</p>

<p align="center">
  <i>"I always try my best!"</i><br>
  <sub>Still training. Check back for the next epoch.</sub>
  <br><br>
  <img src="https://komarev.com/ghpvc/?username=thanhanDemon2003&label=PROFILE%20VIEWS&color=3DFFA0&labelColor=0B1510&style=flat-square" alt="Profile views">
</p>
