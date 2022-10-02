# LIVE: The Light in Venus Exploration 

## Team

We are a team of mechatronics engineers that seeks to solve space problems, and 
in this competition, NASA gives us the opportunity to solve them.

We developed an energy storage system based on lithium-sulfur batteries to 
supply energy for missions to Venus for landers and rovers, making them able to 
rely on energy resources for much longer than we have been able to achieve since 
the first missions began in 1961 with the Venera 1.

This system consists of the same technology with two applications, the main one 
being an independent energy storage system and the secondary one, a system that 
could be installed in future missions to landers, in this case we referred to 
the Venera lander 13 and 14, without However, this alternative is functional 
for future DaVinci and Zephyr missions.

We learned a lot, this has been one of the most demanding challenges in 
scientific and investigative terms given the hostile conditions of Venus and 
the usual factors in the aerospace industry.

Thank you for reading! <3

## Introduction to the problem

Venus has a size, mass and internal composition similar to Earth, however, 
everything else that makes up this interesting planet makes reconnaissance and 
exploration missions impossible for researchers and scientists who seek to know 
more about its composition of its atmosphere and its evolution, 
gas composition, among others.

![The second planet from the Sun and Earth's closest planetary neighbor, Venus.](./images/venus.jpg)
**Figure TODO** - 

Space research, and therefore human curiosity, has no limits, so atmospheric, 
pressure and temperature conditions have not been an excuse to carry out space 
missions related to Venus.

Our team's challenge is to develop an energy storage system for a surface 
lander or a rover that stays on the surface of Venus for at least 60 days, thus 
providing a solution for viable long-term energy storage.

![The Apollo 16 Extended Apollo Lunar Module, a lunar lander](./images/Apollo.jpg)
**Figure TODO** - The Apollo 16 Extended Apollo Lunar Module

The objectives that the competition exposes us are based on selecting 
technologies that are consistent with the challenge, the things that we had in 
mind when developing the solution are the following:

- Energy storage
- Power source
- Effective applicability of the solution on venus
- Self-discharge rate
- Volume
- Dough
- Operation temperature range
- Usage of protective enclosure
- Whether the system can be recharged
- Whether the system uses in situ resources from Venus (e.g., CO2)
- Whether the system can tolerate the forces and vibrations due to launch, reentry, descent, and landing
- Whether the system can tolerate partial failure and still provide energy

## State-of-Art

### **Venera Missions**

Missions to venus take place since 1961 with Venera 1, however, the first 
mission accomplished was with Mariner 2 on December 14, 1962, acquiring data on 
the surface and atmosphere of venus.

One of the most important missions was that of Venera 4, it was a probe in the 
Soviet Venera program for the exploration of Venus. This probe consisted of a 
special landing module to enter the atmosphere of Venus.

This mission allowed us to learn about the temperature and atmospheric 
composition of Venus in a much more precise way.

![Venera 4 model](./images/venera.jpg)
**Figure TODO** - Venera 4 model.

Missions like this one are state of the art for this research, since although 
they differ from energy storage, they allow us to investigate previously proven 
components, such as the sodium-sulfur batteries used in the Sodium Sulfur 
Battery Cell Experiment (NaSBE) in 1996 through a paper published by Ford Motor Company. 

### **Automaton Rover for Extreme Environments (AREE)**

![Automaton Rover for Extreme Environments (AREE)](./images/aree.png)
**Figure TODO** - Automaton Rover for Extreme Environments (AREE) graphical representation.

NASA Jet Propulsion Laboratory designed a concept of automaton rover based on 
ancient mechanical computers with modern manufacturing technology to enable the 
exploration of Venus, known for being one of the most extreme environments in 
the Solar System. <sup>[TODO](https://www.nasa.gov/feature/automaton-rover-for-extreme-environments-aree/)</sup>

AREE uses a hybrid energy storage system made up of a Composite Spring and 
Sodium Metal Chloride Batteries for the advantages that both bring since the 
automaton uses its mechanical energy supply directly to power its locomotion 
system. The instruments that cannot use mechanical energy are powered by 
batteries, which also have a greater energy density than the mechanical energy 
storage system. <sup>[TODO](https://www.nasa.gov/sites/default/files/atoms/files/niac_2016_phasei_saunder_aree_tagged.pdf)</sup>

Hostile Environments Resistance Batteries

## Storage and Source Selection

To promote future missions such as DAVINCI, our team set out to investigate the 
different types of energy storage, based on the new explorations that need to 
be carried out on the surface of Venus.

This research takes place on the resources provided for the competition, the 
experience we have accumulated participating in the previous years and the 
professional knowledge that we were able to apply in academic investigation.

Our investigation began with the following sections:

- Thermal batteries (mainly LiCoS2)
- Sodium-sulphur batteries
- Sodium Metal Chloride Battery
- Lithium Carbonate Battery
- Lithium sulfide batteries

![Sodium sulfur battery cell diagram](./images/NaS.png)
**Figure TODO** - Diagram of the Sodium sulfur battery cell diagram.

Assessing the sections exposed in the competition, and the following:

- Storage Capacity energy
- Source of energy
- Rate of use
- Self-discharge rate
- Whether the system can be recharged
- Using the energy released on atmospheric entry and descent

Using the resources **(Batteries for Venus Surface Operation and Energy Storage 
Technologies for Future Planetary Science Missions)** We were able to learn 
more about the applications and limitations of each type of battery.

Most batteries were discarded due to their inefficiency in terms of energy 
density compared to the others, the main comparison arose between:

A.- Lithium sulfide batteries
B.- Sodium-sulphur batteries
C.- Lithium Carbonate Battery

After further investigation of possible options, Lithium Carbonate Battery (C) 
was dropped due to a lack of application-related research that limits our scope 
and appreciation of this alternative.

Sodium-sulfur (B) batteries, due to their chemical composition, are an 
excellent candidate for this application, being one of the few options that 
have already been implemented in previous missions **** (Attach bibliography 
of previous missions), however, It has a lower power density than options such 
as lithium sulfide batteries (A) and has brittleness in the solid beta-alumina 
electrolyte.


Lithium sulfide batteries have been part of the biggest changes in different 
technological sectors in recent years, from electric vehicles, consumer 
electronics and space is no exception.

Later in the section on "Energy Storage Type" we will be explaining how this 
selection will help us effectively meet the challenge

## Materials Selection

The batteries to be used are based on Lithium-Sulfur

One of the reasons is that sulfur is an abundant element so it’s more 
affordable than cobalt used in Li-Ion cells. On top of that, Li-S cells are 
safer and more environmentally friendly. But the main advantage of this 
technology is the high energy density: around 5 times higher than Li-Ion cells. <sup>[TODO](https://www.e3s-conferences.org/articles/e3sconf/abs/2017/04/e3sconf_espc2017_08006/e3sconf_espc2017_08006.html)</sup>

A Lithium-Sulfur Battery (LSB) is a secondary battery composed of lithium metal anode and sulfur-based cathode, as seen on the following picture.

![Sodium sulfur battery cell diagram](./images/LiS_C_D_cycle.png)
**Figure TODO** - The typical charge -discharge curve of lithium -sulfur batteries. Extracted from [Research Gate](https://www.researchgate.net/figure/The-typical-charge-discharge-curve-of-lithium-sulfur-batteries_fig1_332641982).

As seen, the overall capacity of a cell is reached when the lower potential (voltage) is obtained too during the final discharge stage.

### 1. Cathode materials

The material of excellence for this purpose is elemental sulfur due to its high theoretical specific capacity when combined with lithium, and the fact that it is very low cost and non-toxic.

### 2. Anode materials

When reacting with lithium (the anode), the sulfur prevents the formation of Li dendrites in a great extent due to the dissolved polysulfides (PS). This prevents efficiency problems.

### 3. Electrolyte

A favorable selection for electrolyte solvents is the **dimethyl ether (DME)**, and **1, 3-dioxolane (DOL)**. But its proved that the best choice is the **Lithium trifluoromethanesulfonate (LiSO<sub>3</sub>CF<sub>3</sub>)**.


### 4. Chamber

Due to the extreme environment of Venus, the batteries needs to be located in a 
camera capable of resisting high temperatures, pressure, and its acidic 
atmosphere. For this task, the material selected was **Inconel** alloy 718, which 
is a high-strength, corrosion resistant nickel chromium material that can be 
used at -423°F at 1300°F (commonly used for aerospace applications). <sup>[TODO](https://www.specialmetals.com/documents/technical-bulletins/inconel/inconel-alloy-718.pdf)</sup>

## Process Selection




## Design



### Energy Storage Type

### Materials

### Working Principle

## Solution

## Conclusion

## Future Lines

## References

<!-- State of Artistica -->
- [Automaton Rover for Extreme Environments (AREE)](https://www.nasa.gov/feature/automaton-rover-for-extreme-environments-aree/)
- [AUTOMATON ROVER FOR EXTREME ENVIRONMENTS](https://www.nasa.gov/sites/default/files/atoms/files/niac_2016_phasei_saunder_aree_tagged.pdf)
<!--  -->
2. [High specific energy Lithium Sulfur cell for space application](https://www.e3s-conferences.org/articles/e3sconf/abs/2017/04/e3sconf_espc2017_08006/e3sconf_espc2017_08006.html)

- [1] [Space Food - NASA](https://www.nasa.gov/content/space-food-systems)
- [2] [Growing Plants in Space - NASA](https://www.nasa.gov/content/growing-plants-in-space)
- [3] [Veg-03 Plant Pillows Readied at Kennedy Space Center for Trip to Space Station – Kennedy Space Center (nasa.gov)](https://blogs.nasa.gov/kennedy/2016/04/08/veg-03-plant-pillows-readied-at-kennedy-space-center-for-trip-to-space-station/)






No sé cómo poner referencias, :v


https://ntrs.nasa.gov/api/citations/19970013741/downloads/19970013741.pdf
https://web.archive.org/web/20161228043210/http://astronautix.com/v/venera1vv-67.html
https://web.archive.org/web/20140222000836/http://www.laspace.ru/rus/venera4.php

Lithium-sulphur batteries: opportunities and challenges for
space applications  de Géraldine Palissat* 

High specific energy Lithium Sulfur cell for space application
Bruno Samaniego(1), Emmanuelle Carla (1), Laura O’Neill (2), Maria Nestoridi (3)

Energy Storage Technologies
for Future Planetary Science Missions
(JPL D-101146)

High Specific Energy Lithium Primary Batteries as Power Sources
for Deep Space Exploration
Frederick C. Krause,1 John-Paul Jones,1,∗ Simon C. Jones,1 Jasmina Pasalic,1
Keith J. Billings,1 William C. West,1 Marshall C. Smart,1,∗ Ratnakumar V. Bugga,1,∗
Erik J. Brandon, 1,∗,z and Mario Destephen2


https://www.haynesintl.com/tech-briefs/high-temperature-alloys/high-temperature-alloy-applications/high-temperature-alloys-for-industrial-applications-(H-3116)


https://www.sciencedirect.com/topics/materials-science/high-temperature-alloys
