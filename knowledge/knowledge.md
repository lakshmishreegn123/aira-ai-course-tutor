# BCS515B Artificial Intelligence: Course Notes for AIRA

## Course information
Course: Artificial Intelligence. Course code: BCS515B. Semester: V, 2022 Scheme, VTU. Department of Information Science and Engineering, RV Institute of Technology and Management (RVITM), Bengaluru.
Notes covered here: Module 1 (Introduction to AI and Intelligent Agents) and Module 2 (Problem-Solving and Uninformed Search).
Marks, attendance and grades are not covered here. Students should ask their faculty.
(Source: class notes, Modules 1 and 2, prepared by Prof. Samatha R Swamy and Prof. Avinash N Rao)

---

# MODULE 1: INTRODUCTION AND INTELLIGENT AGENTS

## What is AI
What it is: AI is the branch of computer science that builds machines which act intelligently, and tries to understand intelligence at the same time.
Key points: It covers wide topics (learning, perception) and narrow ones (chess, theorem proving, driving, diagnosing disease). It applies to almost any intellectual task. Machines that improve using the data they collect also count as AI.
(Source: class notes, Module 1; Russell and Norvig, AIMA, Ch. 1)

## Four approaches to AI
What it is: AI definitions can be sorted along two questions: does the system think or act, and does it copy humans or follow an ideal standard (rationality)?
Key points:
- Acting humanly: the Turing Test approach.
- Thinking humanly: the cognitive modeling approach.
- Thinking rationally: the "laws of thought" approach.
- Acting rationally: the rational agent approach.
Remember: human-centred approaches rely on experiments and observation; the rational approach uses mathematics and engineering.
(Source: class notes, Module 1; AIMA Ch. 1)

## Acting humanly: the Turing Test
What it is: A test proposed by Alan Turing in 1950 to give a practical meaning to "intelligence".
How it works: A human interrogator asks written questions. If the interrogator cannot tell whether a person or a computer answered, the computer passes.
Key points: The computer needs natural language processing, knowledge representation, automated reasoning and machine learning. The total Turing Test also adds a video signal and physical objects, so the computer needs computer vision and robotics too.
(Source: class notes, Module 1; AIMA Ch. 1)

## Thinking humanly: cognitive modeling
What it is: Building programs that think the way humans do, which first requires knowing how humans think.
Key points: Ways to study the mind are introspection, psychological experiments and brain imaging. If a program's input-output behaviour matches human behaviour, that is evidence its mechanisms may resemble human ones.
Example: Newell and Simon's General Problem Solver (GPS) compared its reasoning steps with the steps humans took on the same problems.
Remember: cognitive science mixes AI computer models with psychology experiments.
(Source: class notes, Module 1; AIMA Ch. 1)

## Thinking rationally: laws of thought
What it is: The idea that intelligence means correct reasoning, starting from Aristotle's syllogisms (for example: Socrates is a man, all men are mortal, so Socrates is mortal). This led to the field of logic.
Key points: Two obstacles: (1) it is hard to turn informal or uncertain knowledge into formal logic; (2) solving a problem in principle is very different from solving it in practice.
(Source: class notes, Module 1; AIMA Ch. 1)

## Acting rationally: the rational agent approach
What it is: An agent is something that acts. A rational agent acts to achieve the best outcome, or the best expected outcome when things are uncertain.
Key points: Agents are expected to operate on their own, perceive the environment, persist over time, adapt to change and pursue goals. Correct reasoning is one way to act rationally, but not the only way, because sometimes there is no provably correct action and something must still be done.
Why it is preferred: it is more general than the laws-of-thought approach, and the standard of rationality is mathematically well defined, unlike "human behaviour".
(Source: class notes, Module 1; AIMA Ch. 1)

## Applications of AI today
Key points: Examples in the notes are robotic vehicles (the STANLEY car won the 2005 DARPA Grand Challenge), speech recognition, autonomous planning and scheduling (NASA's Remote Agent), game playing (IBM Deep Blue beat Kasparov), spam fighting using learning algorithms, logistics planning (the DART tool), robotics (Roomba vacuum cleaners) and machine translation.
(Source: class notes, Module 1; AIMA Ch. 1)

## Agent, environment, percept and agent function
What it is: An agent is anything that perceives its environment through sensors and acts on it through actuators.
Key points:
- Human agent: eyes and ears are sensors; hands and legs are actuators.
- Robotic agent: cameras and range finders are sensors; motors are actuators.
- Software agent: keystrokes, files and network packets are inputs; screen output, files and network packets are actions.
- Percept: what the agent senses at one moment. Percept sequence: everything it has sensed so far.
- Agent function: an abstract mapping from percept sequences to actions. Agent program: the real code that implements it on a machine.
(Source: class notes, Module 1; AIMA Ch. 2)

## The vacuum-cleaner world
What it is: A simple example world with two squares, A and B.
Key points: The agent senses its location and whether the square is dirty. Its actions are Left, Right, Suck and do nothing. A simple agent function is: if the square is dirty, suck; otherwise move to the other square.
(Source: class notes, Module 1; AIMA Ch. 2)

## Rationality and performance measure
What it is: A rational agent does the right thing. "Right" is judged by a performance measure that scores the sequence of environment states.
Key points: What is rational at a given time depends on four things: (1) the performance measure, (2) the agent's prior knowledge of the environment, (3) the actions it can perform, (4) its percept sequence so far. A rational agent picks the action expected to maximise its performance measure given that evidence.
Example: Rewarding a vacuum agent for dirt collected is a bad measure, because it could dump dirt and clean it again. A better measure gives one point per clean square at each time step. Design the measure around what you want in the environment, not how you think the agent should behave.
(Source: class notes, Module 1; AIMA Ch. 2)

## Omniscience, learning and autonomy
Key points: An omniscient agent knows the actual outcome of its actions, which is impossible in reality. Rationality maximises expected performance; perfection maximises actual performance. Information gathering (acting to improve future percepts) and exploration are part of rationality. An agent that relies only on its designer's built-in knowledge lacks autonomy; a rational agent should learn to make up for incomplete knowledge.
(Source: class notes, Module 1; AIMA Ch. 2)

## PEAS description of a task environment
What it is: PEAS stands for Performance measure, Environment, Actuators, Sensors. It specifies the task an agent is built for.
Example (automated taxi): Performance: reach the right destination, be safe, be fast, save fuel, obey traffic laws, keep passengers comfortable, earn profit. Environment: roads, other traffic, pedestrians, passengers, weather. Actuators: accelerator, steering, brakes, display or speech output. Sensors: cameras, sonar or infrared, speedometer, accelerometer, GPS, engine sensors, keyboard or microphone.
Remember: PEAS = Performance, Environment, Actuators, Sensors.
(Source: class notes, Module 1; AIMA Ch. 2)

## Properties of task environments
What it is: Environments are classified along seven pairs of properties.
Key points:
- Fully vs partially observable: do the sensors show the complete state? Noisy sensors or missing data make it partially observable. No sensors at all means unobservable.
- Single agent vs multiagent: a crossword is single agent; chess is a competitive two-agent environment; taxi driving is partly cooperative and partly competitive.
- Deterministic vs stochastic: deterministic if the next state is fully set by the current state and the action. Taxi driving is stochastic. "Nondeterministic" lists possible outcomes without probabilities.
- Episodic vs sequential: in episodic tasks each decision is independent (for example classification); in sequential tasks the current decision affects future ones (chess, taxi).
- Static vs dynamic: dynamic if the environment can change while the agent is deciding (taxi). Semidynamic if only the score changes with time (chess with a clock). A crossword is static.
- Discrete vs continuous: chess has a finite set of states; taxi driving has continuous speed, position and steering.
- Known vs unknown: in a known environment the outcomes of actions are given. This is different from observability: solitaire is known but partially observable; a new video game can be unknown but fully observable.
(Source: class notes, Module 1; AIMA Ch. 2)

## Agent programs and the table-driven agent
What it is: The agent program takes the current percept as input. If decisions need the whole history, the agent must remember percepts. A table-driven agent stores the percept sequence and looks up an action in a table.
Key points: It does implement the desired function, but a table for every possible percept sequence is far too large to build in practice. The four basic kinds of agent programs are simple reflex, model-based reflex, goal-based and utility-based.
(Source: class notes, Module 1; AIMA Ch. 2)

## Simple reflex agent
What it is: Chooses actions using only the current percept and ignores the history, through condition-action rules (if condition, then action).
Example: If the car in front is braking, then brake. The vacuum agent that sucks when dirty and moves when clean.
Key points: Simple, but it works properly only in a fully observable environment. In partially observable ones it can get stuck in infinite loops. Randomising actions can help it escape.
(Source: class notes, Module 1; AIMA Ch. 2)

## Model-based reflex agent
What it is: Keeps an internal state that tracks the parts of the world it cannot see now, built from the percept history.
Key points: It needs a model of the world, meaning two kinds of knowledge: how the world changes by itself, and how the agent's own actions affect the world. The function UPDATE-STATE builds the new internal state from the old state, the latest action and the new percept.
(Source: class notes, Module 1; AIMA Ch. 2)

## Goal-based agent
What it is: Uses a goal, a description of desirable situations, together with its model to choose actions.
Example: At a road junction the taxi needs its destination to decide whether to turn left, right or go straight.
Key points: Search and planning are the AI subfields that find action sequences to reach goals. It looks less efficient but is more flexible: changing the goal changes the behaviour, and updating knowledge (for example brakes work worse in rain) changes behaviour automatically, whereas a reflex agent would need many rules rewritten.
(Source: class notes, Module 1; AIMA Ch. 2)

## Utility-based agent
What it is: Goes beyond goals by scoring how good each outcome is, using a utility function.
Key points: Goals only give a rough "happy or unhappy" split, but many routes reach the destination, and some are faster, safer or cheaper. The utility function internalises the performance measure. A rational utility-based agent picks the action with the highest expected utility, which also handles uncertainty and conflicting goals.
(Source: class notes, Module 1; AIMA Ch. 2)

## Learning agent
What it is: An agent that improves with experience. It has four components.
Key points:
- Performance element: chooses the external actions (what we earlier treated as the whole agent).
- Learning element: makes improvements using feedback from the critic.
- Critic: tells the learning element how well the agent is doing against a fixed performance standard.
- Problem generator: suggests exploratory actions that lead to new and informative experiences.
(Source: class notes, Module 1; AIMA Ch. 2)

## How agent components represent the world
What it is: Three ways of representing states, in increasing order of complexity and expressive power.
Key points:
- Atomic: each state is an indivisible black box (for example just the name of a city). Used by search, game playing, hidden Markov models and Markov decision processes.
- Factored: each state is a set of variables with values (for example GPS location and fuel level). Used by constraint satisfaction, propositional logic, planning, Bayesian networks and machine learning. It can also represent uncertainty.
- Structured: objects and the relationships among them are described explicitly. Used by relational databases, first-order logic and much of natural language understanding.
(Source: class notes, Module 1; AIMA Ch. 2)

---

# MODULE 2: PROBLEM-SOLVING AND UNINFORMED SEARCH

## Problem-solving agent
What it is: An agent that follows "formulate, search, execute".
How it works:
1. Goal formulation: decide the goal from the current situation and the performance measure.
2. Problem formulation: decide which actions and states to consider, given the goal.
3. Search: look for a sequence of actions that reaches the goal. The output is a solution.
4. Execution: carry out the solution's actions, then formulate a new goal.
(Source: class notes, Module 2; AIMA Ch. 3)

## Well-defined problem (five components)
What it is: A problem is formally defined by five parts. The class example is travelling from Arad to Bucharest in Romania.
Key points:
- Initial state: where the agent starts, for example In(Arad).
- Actions: ACTIONS(s) gives the actions applicable in state s.
- Transition model: RESULT(s, a) gives the state that results from doing action a in state s. States reachable by one action are successors.
- Goal test: checks whether a state is a goal.
- Path cost: a number for each path. Step cost c(s, a, s') is the cost of one action. Total path cost is the sum of step costs.
Also: the initial state, actions and transition model together define the state space, a graph whose nodes are states and links are actions. A path is a sequence of states joined by actions.
Remember: initial state, actions, transition model, goal test, path cost.
(Source: class notes, Module 2; AIMA Ch. 3)

## Formulating problems and abstraction
What it is: A formulation is an abstract model, not the real world. Abstraction means removing detail from a representation.
Key points: An abstraction is valid if any abstract solution can be expanded into a solution in the detailed world. It is useful if carrying out each abstract action is easier than the original problem. A good abstraction removes as much detail as possible while staying valid and useful.
Example: In the route problem, state In(Arad) ignores the weather, the radio and the scenery.
(Source: class notes, Module 2; AIMA Ch. 3)

## Toy problems versus real-world problems
What it is: A toy problem has a concise, exact description and is used to compare algorithms. A real-world problem is one whose solutions people actually care about, and it usually has no single agreed description.
(Source: class notes, Module 2; AIMA Ch. 3)

## Vacuum world problem formulation
Key points:
- States: agent location and dirt locations. With 2 squares there are 2 x 2^2 = 8 states; with n squares there are n x 2^n states.
- Initial state: any state.
- Actions: Left, Right, Suck (larger worlds may add Up and Down).
- Transition model: actions have the expected effect, except moving Left in the leftmost square, Right in the rightmost square, or sucking in a clean square, which do nothing.
- Goal test: all squares are clean.
- Path cost: each step costs 1.
(Source: class notes, Module 2; AIMA Ch. 3)

## 8-puzzle problem formulation
What it is: A 3 x 3 board with eight numbered tiles and one blank. A tile next to the blank can slide into it. The aim is to reach a given goal arrangement.
Key points:
- States: the position of each tile and the blank.
- Initial state: any state (only half of all initial states can reach a given goal).
- Actions: move the blank Left, Right, Up or Down.
- Transition model: returns the state after the move.
- Goal test: matches the goal configuration.
- Path cost: each step costs 1.
Also: it belongs to the sliding-block puzzles, which are NP-complete. The 8-puzzle has 181,440 reachable states.
(Source: class notes, Module 2; AIMA Ch. 3)

## 8-queens problem formulation
What it is: Place eight queens on a chessboard so that no queen attacks another (same row, column or diagonal).
Key points: Two kinds of formulation: incremental (start with an empty board and add a queen at each step) and complete-state (start with all eight queens placed and move them). The path cost does not matter; only the final state counts.
- Simple incremental formulation: any arrangement of 0 to 8 queens is a state; add a queen to any empty square; about 1.8 x 10^14 sequences to check.
- Better formulation: one queen per column in the leftmost columns, and never place a queen on an attacked square. This cuts the state space to 2,057 states.
(Source: class notes, Module 2; AIMA Ch. 3)

## Knuth's toy problem
What it is: Starting from the number 4, apply factorial, square root and floor operations to reach any desired positive integer.
Key points: States: positive numbers. Initial state: 4. Actions: factorial (integers only), square root, floor. Goal test: the state is the desired integer. It shows how an infinite state space can arise.
(Source: class notes, Module 2; AIMA Ch. 3)

## Real-world problems
Key points:
- Airline travel: a state holds the location, the current time and extra history (fare details); actions are flights leaving after the current time; path cost mixes money, waiting time, flight time and more.
- Touring problems: like route finding, but each state must also record the set of cities already visited.
- Traveling salesperson problem (TSP): visit each city exactly once and find the shortest tour. It is NP-hard. It is also used to plan the movement of circuit-board drills.
- Robot navigation: movement in continuous space with infinitely many actions and states, so special techniques are needed to make the search space finite.
(Source: class notes, Module 2; AIMA Ch. 3)

## Searching for solutions: search tree, frontier and explored set
What it is: Search algorithms consider possible action sequences. These sequences form a search tree with the initial state as the root, actions as branches and nodes as states.
Key points:
- Expanding a node means applying every legal action to it, which generates child nodes.
- State space has states and actions; the search tree has nodes and actions. A node is bookkeeping and a state is a world configuration, so two nodes can hold the same state.
- Tree-search algorithms share one structure and differ only in the search strategy (which node to expand next).
- Redundant paths are avoided by keeping an explored set (also called the closed list). This turns TREE-SEARCH into GRAPH-SEARCH.
- The frontier is the set of generated but not yet expanded nodes. It separates the explored region from the unexplored region.
(Source: class notes, Module 2; AIMA Ch. 3)

## Node data structure and queues
Key points: Each node n stores n.STATE, n.PARENT, n.ACTION and n.PATH-COST (g(n)). Parent pointers let us rebuild the solution path from the goal node back to the root. The frontier is stored in a queue with the operations EMPTY?, POP and INSERT.
(Source: class notes, Module 2; AIMA Ch. 3)

## Measuring search performance
What it is: Four criteria to evaluate a search algorithm.
Key points:
- Completeness: does it always find a solution when one exists?
- Optimality: does it find the best (lowest-cost) solution?
- Time complexity: how long does it take (usually the number of nodes generated)?
- Space complexity: how much memory does it need (usually the maximum nodes stored)?
Terms used in complexity: b is the branching factor (maximum number of successors of a node), d is the depth of the shallowest goal node, m is the maximum length of any path.
(Source: class notes, Module 2; AIMA Ch. 3)

## Uninformed search (overview)
What it is: Uninformed (blind) strategies have no extra information about states beyond the problem definition. They can only generate successors and tell a goal from a non-goal.
Key points: The strategies covered are breadth-first search, depth-first search, iterative deepening, depth-limited search, uniform-cost search and bidirectional search.
(Source: class notes, Module 2; AIMA Ch. 3)

## Breadth-first search (BFS)
What it is: Expands the root first, then all its successors, then their successors, so all nodes at one depth are expanded before the next depth.
How it works: The frontier is a FIFO queue, so the shallowest unexpanded node is expanded first. The goal test is applied when a node is generated.
Properties: Complete (if the branching factor is finite). Optimal when all steps cost the same, because it expands the shallowest node first. Time O(b^d). Space O(b^d).
Advantages: Finds a solution if one exists, and finds the one with the fewest steps.
Disadvantages: Needs a lot of memory because each level must be kept to expand the next, and it is slow when the solution is deep. Memory is the bigger problem than time.
(Source: class notes, Module 2; AIMA Ch. 3)

## Depth-first search (DFS)
What it is: Always expands the deepest node in the frontier, then backs up to the next deepest node that still has unexplored successors.
How it works: The frontier is a LIFO queue (stack), so the most recently generated node is expanded first.
Properties: Not complete (it can loop forever or go down an infinite path). Not optimal. Time O(b^m). Space O(bm), which is small.
Advantages: Needs very little memory (only the path from the root to the current node) and can reach the goal quickly if it takes the right path.
Disadvantages: States may repeat, it may go into an infinite loop, and there is no guarantee of a solution.
(Source: class notes, Module 2; AIMA Ch. 3)

## Depth-limited search (DLS)
What it is: Depth-first search with a fixed depth limit l, where nodes at depth l are treated as having no successors.
Key points: The limit fixes the infinite-path problem. But it is incomplete if l is less than d (the goal is beyond the limit) and non-optimal if l is greater than d. Time O(b^l). Space O(bl). It can end with two kinds of failure: failure (no solution) and cutoff (no solution within the limit). DFS is the special case where l is infinite.
(Source: class notes, Module 2; AIMA Ch. 3)

## Iterative deepening depth-first search (IDS)
What it is: Runs depth-limited search again and again with limits 0, 1, 2, and so on until the goal is found, which happens when the limit reaches d.
Properties: Complete when the branching factor is finite. Optimal when the path cost is a non-decreasing function of depth. Time O(b^d). Space O(bd).
Advantages: Combines the memory efficiency of DFS with the completeness of BFS.
Disadvantages: States near the top are generated many times. The extra cost is small: with b = 10 and d = 5, IDS generates 123,450 nodes against 111,110 for BFS.
(Source: class notes, Module 2; AIMA Ch. 3)

## Uniform-cost search (UCS)
What it is: Expands the node with the lowest path cost g(n).
How it works: The frontier is a priority queue ordered by g. Two differences from BFS: (1) the goal test is applied when a node is selected for expansion, not when it is generated, because the first goal generated may be on a costlier path; (2) if a cheaper path to a node already in the frontier is found, it replaces the old one.
Example: From Sibiu to Bucharest, the path through Fagaras costs 310 but the path through Rimnicu Vilcea and Pitesti costs 278, so UCS chooses the second.
Properties: Optimal and complete when every step cost is positive (from the textbook). It is the same as BFS when all step costs are equal.
(Source: class notes, Module 2; AIMA Ch. 3)

## Bidirectional search
What it is: Runs two searches at once: one forward from the initial state and one backward from the goal. It stops when the two searches meet.
Properties: Time O(b^(d/2)). Space O(b^(d/2)) (when BFS is used), since at least one search tree must be kept in memory to check for meeting. Completeness and optimality depend on the strategies used in the two searches.
Advantages: Fast, and needs less memory than a single search.
Disadvantages: It is hard to implement, and the goal state must be known in advance.
(Source: class notes, Module 2; AIMA Ch. 3)

## Comparison of uninformed search strategies
What it is: A side-by-side summary. Complete means finds a solution whenever one exists; optimal means finds the lowest-cost solution.

| Strategy | Complete | Optimal | Time | Space |
|---|---|---|---|---|
| Breadth-first | Yes (finite b) | Yes, if all step costs are equal | O(b^d) | O(b^d) |
| Uniform-cost | Yes, if step costs are positive | Yes | depends on the path costs | depends on the path costs |
| Depth-first | No | No | O(b^m) | O(bm) |
| Depth-limited | No, if l is less than d | No | O(b^l) | O(bl) |
| Iterative deepening | Yes (finite b) | Yes, if path cost is non-decreasing with depth | O(b^d) | O(bd) |
| Bidirectional | Depends on the searches used | Depends on the searches used | O(b^(d/2)) | O(b^(d/2)) |

Remember: BFS is safest but memory hungry; DFS is light on memory but risky; IDS combines both; UCS handles different step costs; bidirectional is fastest but needs a known goal.
(Source: class notes, Module 2; AIMA Ch. 3)