# panthera-hybrid-namer

* Use the [here](https://en.wikipedia.org/wiki/Panthera_hybrid) as reference.
* Create a base class **_Panthera_** that has the properties **_name, generation and gender_**.
* Create subclasses of **_Panthera_** class, e.g. **_Lion, Tiger,_** etc.
* **_Panthera_** instances/objects should be sortable when used in the built-in **_sort()_** by generation (first priority)
and name (use __*\__gt__*__, __*\__eq__*__, etc.)
* **_Panthera_** objects can be crossed to generate a next generation hybrid:
** **_Lion + Tigress = Liger_** (gender should be randomly generated)
** You can only cross 2 pantheras that are of different genders