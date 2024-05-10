
1. Introduction
a. Application Overview:
Paprasta kodas, kuris leidžia įvesti daktarus, seseles ir pacientus.
Leidžia sekti ką daktarai ir seseles saugo, kuriam skyriui dirba, leidžia žinoti kokie pacientai ir kokia pas juos problema.

b. Running the Program:
Reikia turėti python instaliuota ir tada paleisti koda per pvz VC Studio.

c. Program Usage:
Suvedami daktarų duomenys, seselių duomenys, pacientų duomenys, paleidžiama programa ir matomi visi rezultatai.

2. Body/Analysis
Functional Requirements Coverage:
Polymorphism: Doctor, nurse ir patient ovverraidina display_info kad parodyti sau specifine informacija.
Abstraction: Person yra abstrakti klasė su abstrakčiu metodu. display_info() yra abstraktus metodas nes pats iš savęs nieko neturi ir jo negalima pakviesti. Subklasės turi 
overraidint jį. 
Inheritance:  Naudojamas kad sukurti subklases:Doctor, Nurse, Patient, kurios paveldi viskas iš Person klasės.
Encapsulation: Klasių atributai name,age yra visose klasėse, bet atributai pvz specialization ar department yra tik jiems priskirtuose klasėse.

Design Patterns
Singleton: Naudojamas Hospital klasei, kad būtų tik viena klasė Hospital per visą kodą. Tai leidžia
visiem pasiekti Hospital klasės datą.
Factory method: Naudojamas StaffFactory ir jos subklasėm. StafFaactory duoda savo subklasėm skeletą,
kurį jos visos turi naudoti. Subklasės naudoja tą skeletą ir prie jo dar dadėda kažka pvz.: Nurse dadėda department.
Tai leidžia sukurti person objekta atskiroje factory klasėke.

3.Results
Manau sekmingai sukūriau programą, kuri leidžia sekti daktarus, seseles ir pacientus.
Sunkiausia kodo dalis turbūt būtų testai ir kad imtų informacija iš failo ir ją dėtu į failą,
nes pirma kartą reikia šiuos būdus naudoti. Taip pat buvo sunku surasti kaip push code to repository.


