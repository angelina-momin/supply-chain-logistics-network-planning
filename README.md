
## 📑 Table of contents
- [🏙️ Introduction](#-introduction)
  - [🛣️ Road Types](#-road-types)
- [🖥️ Computational Task](#-computational-task)
  - [🎯 Objective](#-objective)
  - [📌 Inputs](#-inputs)
  - [📄 Outputs](#-outputs)
- [⚙️ Game Rules](#-game-rules)
- [💡 Considerations for Optimization](#-considerations-for-optimization)
- [📈 Visualization](#-visualization)
- [🚀 Getting Started](#-getting-started)
- [🤝 Contributing](#-contributing)
- [📞 Contact](#-contact)


<!-- ABOUT THE PROJECT -->
## 🏙️ About the project
The project tackles a town road planning problem. In a newly built town with houses, shopping malls, and a centralized city center, roads are the essential backbone that determine its livability and functionality. As urban planners, the task is to intelligently lay down the roads, optimizing for cost and accessibility.

### 🛣️ Road Types:

1. **Local Roads**: 
   - Connect houses to other houses.
   - Link houses to malls.
   
2. **Express Roads**:
   - Bridge malls with other malls.
   - Route malls to the city center.

<!-- ALGORITHMIC DESIGN -->
## 🖥️ The Algorithmic Design

### 🎯 Objective:
Develop an algorithm that efficiently plans the roads, considering various cost scenarios.

### 📌 Inputs:
- `N` house coordinates `(x,y)`.
- `M` mall coordinates `(x,y)`.
- City center coordinates `(x,y)`.

### 📄 Outputs:
- A list of planned local roads.
- A list of planned express roads.
- Total length of the planned local roads.
- Total length of the planned express roads.
- A visualization of the proposed solution.

<!-- GAME RULES -->
## ⚙️ Game Rules:

- **Connectivity**: Every house must connect to every other house.
- **Access to Amenities**: Each house should have a route to at least one mall.
- **Central Access**: Every house must have a road leading to the city center.
- **Travel Definition**: Traveling encompasses moving via local or express roads, and possibly via other houses or malls as intermediaries.
- **Mall Requirement**: Not all malls need a connection.
- **Size Constraints**: Both M and N are expected to be of the order of 10.

<!-- CONSIDERATIONS FOR OPTIMIZATION -->
## 💡 Considerations for Optimization:

The algorithm should optimize the road planning based on the following scenarios:
1. When local roads are much cheaper to build than express roads.
2. When local roads are much more expensive than express roads.
3. When the costs of constructing local and express roads are comparable.

<!-- GETTING STARTED -->
## 🚀 Getting started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

All the packages needed to run the code can be found in [requirements.txt](requirements.txt). To install the prerequisites create a virtual environment first and then run the following command.
  ```
  pip install -r requirements.txt 
  ```

<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ROADMAP -->
## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/speeder-coder/Road-Planning/issues) for a full list of proposed features (and known issues).



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

Project Link: [https://github.com/speeder-coder/Road-Planning](https://github.com/speeder-coder/Road-Planning)




