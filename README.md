# SUPPLY CHAIN LOGISTICS NETWORK README
## 📑 Table of contents

- [📦 Introduction](#-introduction)
  - [🏢 Types of Buildings](#-types-of-buildings)
  - [🚚 Types of Transportation Routes](#-types-of-transportation-routes)
- [🖥️ Computational Task](#-computational-task)
  - [🎯 Objective](#-objective)
  - [📌 Inputs](#-inputs)
  - [📄 Outputs](#-outputs)
- [⚙️ Rules](#-rules)
- [💡 Considerations for Optimization](#-considerations-for-optimization)
- [📈 Visualization](#-visualization)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📞 Contact](#-contact)


<!-- INTRODUCTION -->
## 📦 Introduction
This project addresses the complex challenges associated with supply chain logistics for multinational corporations. 
It offers a solution that strategically plans both local and express delivery routes connecting factories, warehouses, 
and a central distribution hub.

The codebase enables businesses to:

  🗺️ Design Efficient Routes: Determine the most efficient local and express routes between factories, warehouses, 
  and the main distribution center.

  📊 Optimize Costs: Significantly reduce transportation costs by finding the shortest possible routes that 
  meet all business constraints.

  ⏲️ Speed Up Deliveries: By optimizing routes, the code ensures that products move through the supply chain as 
  quickly as possible, reducing lead times.

  🌿 Minimize Environmental Impact: The optimized routes are designed to minimize the distance traveled, 
  reducing the carbon footprint of the logistics network.

<!-- TYPES OF BUILDINGS -->
### 🏢 Types of Buildings:

1. Factories
    Factories are the initial points in the supply chain where raw materials are transformed into products.

2. Warehouses
    Warehouses serve as storage centers where products from factories are stored temporarily before 
    being shipped to the distribution center or directly to the consumers.

3. Distribution Center:
    The main distribution center acts as a hub that receives products from various warehouses and 
    factories and redistributes them to the final consumer locations.

<!-- TYPES OF TRANSPORTATION ROUTES -->
### 🚚 Types of Transportation Routes:

1. Local Routes:
    - Connect factories to their nearest warehouses.
    - Link factories with other factories for component sharing.

2. Express Routes:
    - Connect warehouses to other warehouses for stock balancing.
    - Link each warehouse to the main distribution center.

<!-- ALGORITHMIC DESIGN -->
## 🖥️ The Algorithmic Design

### 🎯 Objective:
Develop an algorithm that efficiently plans the routes connecting factories, warehouses, 
and a central distribution hub such that the total length of routes is minimized, 
subsequently reducing fuel costs.

### 📌 Inputs:
- A set of `N` factory coordinates `(x,y)`.
- A set of `M` warehouse coordinates `(x,y)`.
- The coordinates of the main distribution center `(x,y)`.

### 📄 Outputs:
- A list of established local routes.
- A list of planned express routes.
- Total distance of planned local routes.
- Total distance of planned express routes.
- Visualization of the logistics network.

<!-- RULES -->
## ⚙️ Game Rules:

- **Inter-factory Connectivity**: Every factory must connect to every other factor for efficient component sharing.
- **Factory-warehouse Connectivity**: Each factory must be connected to at least one warehouse to ensure production 
outputs reach storage.
- **Access of warehouse to distribution center**: Every warehouse must have a direct or indirect connection to the main
 distribution center.
- **Inter-warehouse Connectivity**: Not all warehouses need to be connected to each other.
- **Size Constraints**: Both M and N are expected to be of the order of 1.

<!-- CONSIDERATIONS FOR OPTIMIZATION -->
## 💡 Considerations for Optimization:

The algorithm should optimize the road planning based on the following scenarios:
1. When local routes are much cheaper to build than express routes.
2. When local routes are much more expensive than express routes.
3. When the costs of constructing local and express routes are comparable.

<!-- GETTING STARTED -->
## 🚀 Getting started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

All the packages needed to run the code can be found in [requirements.txt](requirements.txt). To install the prerequisites create a virtual environment first and then run the following command.
  ```
  pip install -r requirements.txt 
  ```

<!-- CONTRIBUTING -->
## 🤝 Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<!-- CONTACT -->
## 📞 Contact

Angelina Momin - amomin2630@outlook.com

Project Link: [https://github.com/speeder-coder/supply-chain-logistics-network-planning](https://github.com/speeder-coder/supply-chain-logistics-network-planning)




