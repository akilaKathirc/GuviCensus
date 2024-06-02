
--What is the total population of each district?
select District_code, coalesce(Population, (Male+Female)) as TotalPopulation from census_2011

--How many literate males and females are there in each district?
select District_code,Male_Literate,Female_Literate  from census_2011

SELECT District_code, SUM(Male_Literate) AS Total_Literate_Males, SUM(Female_Literate) AS Total_Literate_Females
FROM Census_2011
GROUP BY District_code;


--What is the percentage of workers (both male and female) in each district?
select District_code
, ((CAST(Male_Workers AS FLOAT) / CAST(Workers AS FLOAT)) * 100)
as maleWorkersPercentage
, ((CAST(Female_Workers AS FLOAT) / CAST(Workers AS FLOAT)) * 100) as femaleWorkersPercentage
from census_2011


--How many households have access to LPG or PNG as a cooking fuel in each district?
select District_code, LPG_or_PNG_Households from census_2011


--What is the religious composition (Hindus, Muslims, Christians, etc.) of each district?

select isnull(Hindus, 0) + isnull(Muslims, 0)+isnull(Christians, 0)+isnull(Sikhs, 0)
+isnull(Buddhists, 0)
+isnull(Jains, 0)+isnull(Others_Religions, 0) as ReligiousPeople  from census_2011

--How many households have internet access in each district?
select District_code, Households_with_Internet from census_2011



--What is the educational attainment distribution (below primary, primary, middle, secondary,
--etc.) in each district?


select
 (isnull(Below_Primary_Education,0)
+isnull(Primary_Education,0)
+isnull(Middle_Education,0)
+isnull(Secondary_Education,0)
+isnull(Higher_Education,0)
+isnull(Graduate_Education,0)
+isnull(Other_Education,0) ) as educationDistribution from census_2011 


--How many households have access to various modes of transportation 
--(bicycle, car, radio, television, etc.) in each district?
select District_code,isnull (Households_with_Bicycle, 0)+
isnull(Households_with_Car_Jeep_Van, 0) as TransportFacility from census_2011

select District_code,isnull (Households_with_Bicycle, 0)+
isnull(Households_with_Car_Jeep_Van, 0) as TransportFacility from census_2011


select 
isnull(Households_with_Bicycle, 0)
+ isnull(Households_with_Car_Jeep_Van, 0)
+ isnull(Households_with_Radio_Transistor, 0)
+ isnull(Households_with_Scooter_Motorcycle_Moped, 0)
+ isnull(Households_with_Telephone_Mobile_Phone_Landline_only, 0)
+ isnull(Households_with_Telephone_Mobile_Phone_Mobile_only, 0)
+ isnull(Households_with_TV_Computer_Laptop_Telephone_mobile_phone_and_Scooter_Car, 0)
+ isnull(Households_with_Television, 0)
+ isnull(Households_with_Telephone_Mobile_Phone, 0)
+ isnull(Households_with_Telephone_Mobile_Phone_Both, 0)
+ isnull(Condition_of_occupied_census_houses_Dilapidated_Households, 0)
+ isnull(Households_with_separate_kitchen_Cooking_inside_house, 0)
+ isnull(Having_bathing_facility_Total_Households, 0)
+ isnull(Having_latrine_facility_within_the_premises_Total_Households, 0) as houseFacilties
from census_2011


--What is the condition of occupied census houses (dilapidated, with separate kitchen, 
--with bathing facility, with latrine facility, etc.) in each district?

select
isnull(Condition_of_occupied_census_houses_Dilapidated_Households,0)
+isnull(Households_with_separate_kitchen_Cooking_inside_house,0)
+isnull(Having_bathing_facility_Total_Households,0)
+isnull(Having_latrine_facility_within_the_premises_Total_Households,0)
from census_2011

--How is the household size distributed (1 person, 2 persons, 3-5 persons, etc.)
--in each district?
select district_code
,Household_size_1_person_Households
,Household_size_2_persons_Households
,Household_size_1_to_2_persons
,Household_size_3_persons_Households
,Household_size_3_to_5_persons_Households
,Household_size_4_persons_Households
,Household_size_5_persons_Households
,Household_size_6_8_persons_Households
,Household_size_9_persons_and_above_Households
from census_2011

--What is the total number of households in each state?
select sum (x.HouseHoldPerDistrict) totalHouseHolds, State_name from
(select State_name
,isnull(Household_size_1_person_Households,0)
+isnull(Household_size_2_persons_Households,0)
+isnull(Household_size_1_to_2_persons,0)
+isnull(Household_size_3_persons_Households,0)
+isnull(Household_size_3_to_5_persons_Households,0)
+isnull(Household_size_4_persons_Households,0)
+isnull(Household_size_5_persons_Households,0)
+isnull(Household_size_6_8_persons_Households,0)
+isnull(Household_size_9_persons_and_above_Households,0) as HouseHoldPerDistrict
from census_2011) x
group by State_name

--How many households have a latrine facility within the premises in each state?
select sum(Having_latrine_facility_within_the_premises_Total_Households), State_name
from census_2011 group by State_name

--What is the average household size in each state?
select avg (x.HouseHoldPerDistrict) AverageHouseHoldSize, State_name from
(select State_name
,isnull(Household_size_1_person_Households,0)
+isnull(Household_size_2_persons_Households,0)
+isnull(Household_size_1_to_2_persons,0)
+isnull(Household_size_3_persons_Households,0)
+isnull(Household_size_3_to_5_persons_Households,0)
+isnull(Household_size_4_persons_Households,0)
+isnull(Household_size_5_persons_Households,0)
+isnull(Household_size_6_8_persons_Households,0)
+isnull(Household_size_9_persons_and_above_Households,0) as HouseHoldPerDistrict
from census_2011) x
group by State_name



--How many households are owned versus rented in each state?

select State_name, sum(Ownership_Owned_Households) OwnedHHold,
sum(Ownership_Rented_Households)RentedHHold from census_2011
group by State_name
--What is the distribution of different types of latrine facilities (pit latrine, flush latrine, etc.) 
--in each state?
select State_name
, sum(Type_of_latrine_facility_Pit_latrine_Households) PL
,sum(Type_of_latrine_facility_Other_latrine_Households) OL
,sum(Type_of_latrine_facility_Night_soil_disposed_into_open_drain_Households) NL
,sum(Type_of_latrine_facility_Flush_pour_flush_latrine_connected_to_other_system_Households) FPFL from census_2011
group by State_name
--How many households have access to drinking water sources near the premises in each state?


select State_name, sum(Location_of_drinking_water_source_Near_the_premises_Households) WaterNearPremises
 from census_2011
group by State_name

--What is the average household income distribution in each state based on the power parity categories?


select State_name
,avg(Power_Parity_Less_than_Rs_45000)  PPLt45000
,avg(Power_Parity_Rs_45000_90000	) [PP_45000_90000]
,avg(Power_Parity_Rs_90000_150000	) [PP_90000_150000	 ]
,avg(Power_Parity_Rs_45000_150000	) [PP_45000_150000	 ]
,avg(Power_Parity_Rs_150000_240000	) [PP_150000_240000 ]
,avg(Power_Parity_Rs_240000_330000	) [PP_240000_330000 ]
,avg(Power_Parity_Rs_150000_330000	) [PP_150000_330000 ]
,avg(Power_Parity_Rs_330000_425000	) [PP_330000_425000 ]
,avg(Power_Parity_Rs_425000_545000	) [PP_425000_545000 ]
,avg(Power_Parity_Rs_330000_545000	) [PP_330000_545000 ]
,avg(Power_Parity_Above_Rs_545000	) from census_2011
group by State_name


--What is the percentage of married couples with different household sizes in each state?

--How many households fall below the poverty line in each state based on the power parity categories?

select state_name, sum(pLPP) from 
(select state_name
,isnull(Power_Parity_Less_than_Rs_45000,0) 
+isnull(Power_Parity_Rs_45000_90000	   ,0) 
+isnull(Power_Parity_Rs_90000_150000   ,0) 
+isnull(Power_Parity_Rs_45000_150000,0) pLPP from census_2011) x
group by State_name
--What is the overall literacy rate (percentage of literate population) in each state?

select State_name, sum(ltPercent) OverallLtR from (
select state_name , ((cast(Literate as float)/cast(Population as float))*100) as ltPercent
from census_2011) x
group by State_name





