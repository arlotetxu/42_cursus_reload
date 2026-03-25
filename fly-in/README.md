*This project has been created as part of the 42 curriculum by joflorid.*

# Fly-In: Drone Pathfinding Simulation

## Description

The "Fly-In" project is a drone simulation challenge designed to test and
optimize pathfinding algorithms in complex, constrained environments.
Its primary goal is to simulate multiple drones navigating a predefined map,
finding the most efficient paths from their starting points to their
respective destinations while adhering to various real-world constraints.

The simulation environment features a graph-based map composed of "hubs"
(nodes) and "connections" (edges). These hubs and connections can have
specific attributes such as capacity limits, different traversal costs based
on zone types (e.g., restricted, priority, blocked), and dynamic states
(e.g., current drone occupancy). The core challenge lies in developing an
algorithm that can efficiently find optimal paths for multiple drones,
avoiding collisions, managing capacities, and minimizing overall simulation
turns.

## Instructions

### Compilation and Installation

This project is written in Python. To set up the environment:

1.  **Clone the repository:**
    ```bash
    git clone git@vogsphere.42urduliz.com:vogsphere/intra-uuid-a58e2972-d195-4c04-8964-40f88e043370-7298216-joflorid fly-in
    cd fly-in
    ```

    **a. Python:**

    2.  **Create and activate a virtual environment (recommended):**
    ```bash
        python3 -m venv venv
        source venv/bin/activate
    ```
    3.  **Install dependencies:**
    ```bash
        pip install -r requirements.txt
    ```

    **b. UV:**

    2.  **Install dependencies:**
    ```bash
        uv sync
    ```
    or
    ```bash
        make install
    ```

### Execution

To run the simulation, you will need to provide a map file. Map files are located in the `maps/` directory and define the hubs, connections, and drone configurations.

```bash
python3 fly-in.py <path/to/map_file.txt>
```

or

```bash
make run
```


**Example:**

```bash
python3 main.py maps/easy/01_linear_path.txt
```


## Algorithm Choices and Implementation Strategy

The core pathfinding mechanism in this project relies on the **A\* search algorithm**.
A\* was chosen for its ability to find the shortest path efficiently by
combining the benefits of Dijkstra's algorithm (guaranteed optimality) and
greedy best-first search (heuristic guidance).

### Graph Representation

The map is represented as a graph where:
*   **Nodes (Hubs):** Each `Hub` object (`src/objs/hub.py`) represents a
location where drones can cross. Hubs store their name, coordinates (`x`, `y`),
zone type, maximum drone capacity (`max_drones`), and a list of neighbors.
*   **Edges (Connections):** Connections between hubs are implicitly defined
within the `neighbors` dictionary of each `Hub`. The cost of traversing a
connection is influenced by the `traversal_cost` of the destination hub and
potentially `max_link_capacity` (though `max_link_capacity` is parsed,
its direct application to edge weights isn't explicitly shown in the `Hub` class).

### A\* Implementation Details

*   **Cost Function (`f_cost`):** Each `Hub` maintains `g_cost` (cost from
start to current hub) and `h_cost` (estimated cost from current hub to goal).
The `f_cost` property calculates `g_cost + h_cost`.
*   **Heuristic Function (`h_cost`):** For grid-based maps (like those implied
by `x`, `y` coordinates), a common and effective heuristic is the
**Manhattan distance** or **Euclidean distance**. Given the `Hub` class
only stores `h_cost` as a value, it's assumed that this value is
pre-calculated or dynamically updated based on the distance to the target hub.
An admissible and consistent heuristic is crucial for A\*'s performance and
optimality guarantees.
*   **Traversal Costs:** The `traversal_cost` property of a `Hub` dynamically
adjusts the cost of entering a hub based on its `zone` type:
    *   `normal`: Cost of 1
    *   `restricted`: Cost of 2 (slower)
    *   `priority`: Cost of 0.8 (preferred)
    *   `blocked`: Infinite cost (impassable)
    This allows A\* to naturally prefer faster zones and avoid blocked areas.
*   **Capacity Constraints:** The `is_crossable` property checks if a hub can
accept more drones (`curr_drones < max_drones`) and is not blocked. This
constraint is critical for multi-drone scenarios, as it prevents drones from
occupying already full hubs. The pathfinding algorithm must account for these
dynamic capacities, potentially re-calculating paths or waiting if a hub is
temporarily full.
*   **Multi-Drone Coordination:** For multiple drones, the A\* algorithm is
likely run iteratively or in a time-dependent manner. This means that the `g_cost`
might not just be the sum of traversal costs but also incorporate waiting
times or penalties for conflicts with other drones. The `max_drones` and
`max_link_capacity` (from map parsing) suggest that the simulation needs to
manage resource contention.

### Implementation Strategy

The strategy involves:
1.  **Robust Map Parsing:** Using `pydantic` for strict validation of map data
(`src/parsing/data_model.py`, `src/parsing/map_parsing.py`) ensures that the
simulation operates on well-formed input, preventing errors early.
2.  **Modular Hub Representation:** The `Hub` class encapsulates all necessary
information and logic for a node in the graph, making the pathfinding logic cleaner.
3.  **Dynamic Cost Calculation:** The `traversal_cost` property allows for
flexible and scenario-specific path costs without altering the core A\* logic.
4.  **Worst-Case Scenario Handling:** The `is_blocked` property and infinite
`traversal_cost` for "blocked" zones ensure that A\* correctly avoids impassable areas.

## Visual Representation Features

The project incorporates a terminal visual representation feature, which
significantly enhances the user experience by providing real-time feedback
on the simulation's progress.


## Resources

*   **A\* Search Algorithm:**
    *   Wikipedia: A\* search algorithm
    *   Drone Flight Planning Algorithm: [https://www.youtube.com/watch?v=8frpg52TzQ8]
    *   Easy A\*: [https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2]
    *   A* Search Algorithm in Python: [https://www.geeksforgeeks.org/python/a-search-algorithm-in-python/]
    *   Algorithm visualizator: [https://qiao.github.io/PathFinding.js/visual/]

*   **Python Libraries:**
    *   Pydantic Documentation - Used for data validation and parsing map files.
    *   Icecream Documentation - Used for enhanced debugging output.

### AI Usage

*   To query the best fitting algorithms for this project.
*   To provide an introduction to the A* algorithm and its fine-tuning.
*   To unblock scenarios during the coding process.

