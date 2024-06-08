sql_queries_dict = {
    "1.Total population of each district": """select District_code
                                            , coalesce(Population, (isnull(Male, 0)+isnull(Female, 0))) as TotalPopulation from census_2011
                                            order by district_code desc""",
    "2.Literate males and females in each district": """SELECT District_code, SUM(Literate_Male) 
                                                AS Total_Literate_Males, SUM(Literate_Female) AS Total_Literate_Females
                                            FROM Census_2011
                                            GROUP BY District_code""",
    "3.Workers percentage in each district": """select District_code
                                                , ((CAST(Male_Workers AS FLOAT) / CAST(Workers AS FLOAT)) * 100)
                                                as maleWorkersPercentage
                                                , ((CAST(Female_Workers AS FLOAT) / CAST(Workers AS FLOAT)) * 100) as femaleWorkersPercentage
                                                from census_2011""",

    "4. households access to LPG/PNG in each district": """select District_code, sum(LPG_or_PNG_Households) TotalHouseHolds from census_2011 GROUP BY District_code;""",
    
    "5.Religious composition - District": """select district_code,sum(isnull(Hindus, 0) + isnull(Muslims, 0)+isnull(Christians, 0)+isnull(Sikhs, 0)
                                            +isnull(Buddhists, 0)
                                            +isnull(Jains, 0)+isnull(Others_Religions, 0)) as ReligiousPeople  from census_2011
                                            group by district_code""",
   
    "6. Households with internet access": """select District_code, sum(Households_with_Internet) TotalInternetHH from census_2011 group by District_code""",
    "7. Educational attainment distribution": """select District_code, sum
                                                (isnull(Below_Primary_Education,0)
                                                +isnull(Primary_Education,0)
                                                +isnull(Middle_Education,0)
                                                +isnull(Secondary_Education,0)
                                                +isnull(Higher_Education,0)
                                                +isnull(Graduate_Education,0)
                                                +isnull(Other_Education,0) ) as educationDistribution from census_2011 group by District_code""",
    "8. Households with access to modes of transportation ": """select District_code,sum(
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
                                                                + isnull(Having_latrine_facility_within_the_premises_Total_Households, 0)) as houseFacilties
                                                                from census_2011 group by District_code""",
    "condition of occupied census houses": """
                                                select District_code,sum(
                                                isnull(Condition_of_occupied_census_houses_Dilapidated_Households,0)
                                                +isnull(Households_with_separate_kitchen_Cooking_inside_house,0)
                                                +isnull(Having_bathing_facility_Total_Households,0)
                                                +isnull(Having_latrine_facility_within_the_premises_Total_Households,0))  as OccupiedHouses
                                                from census_2011  group by District_code""",
    "household size distributed": """select district_code
                                    ,sum(Household_size_1_person_Households) one
                                    ,sum(Household_size_2_persons_Households) two
                                    ,sum(Household_size_1_to_2_persons) oneToTwo
                                    ,sum(Household_size_3_persons_Households) three
                                    ,sum(Household_size_3_to_5_persons_Households) threeToFive
                                    ,sum(Household_size_4_persons_Households) Four
                                    ,sum(Household_size_5_persons_Households) Five
                                    ,sum(Household_size_6_8_persons_Households) SixToEight
                                    ,sum(Household_size_9_persons_and_above_Households) nine
                                    from census_2011  group by District_code""",
    "total number of households in each state": """select sum (x.HouseHoldPerDistrict) totalHouseHolds, [State/UT] from
                                                    (select [State/UT]
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
                                                    group by [State/UT]""",
    "households have a latrine facility within the premises in each state": """select sum(Having_latrine_facility_within_the_premises_Total_Households) HouseHolds, [State/UT]
                                                                                from census_2011 group by [State/UT]""",
    "Average household size in each state": """select avg (x.HouseHoldPerDistrict) AverageHouseHoldSize, [State/UT] from
                                            (select [State/UT]
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
                                            group by [State/UT]""",
    "households are owned versus rented in each state": """select [State/UT], sum(Ownership_Owned_Households) OwnedHHold,
                                                            sum(Ownership_Rented_Households)RentedHHold from census_2011
                                                            group by [State/UT]""",
    "distribution of different types of latrine facilities in each state": """select [State/UT], sum(Ownership_Owned_Households) OwnedHHold,
                                                                            sum(Ownership_Rented_Households)RentedHHold from census_2011
                                                                            group by [State/UT]""",
    "households have access to drinking water": """select [State/UT], sum(Location_of_drinking_water_source_Near_the_premises_Households) WaterNearPremises
                                                    from census_2011
                                                    group by [State/UT]""",
    "average household income distribution": """select [State/UT]
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
                                                group by [State/UT]""",
    "households fall below the poverty line": """select [State/UT], sum(pLPP) from 
                                                (select [State/UT]
                                                ,isnull(Power_Parity_Less_than_Rs_45000,0) 
                                                +isnull(Power_Parity_Rs_45000_90000	   ,0) 
                                                +isnull(Power_Parity_Rs_90000_150000   ,0) 
                                                +isnull(Power_Parity_Rs_45000_150000,0) pLPP from census_2011) x
                                                group by [State/UT]""",
    "overall literacy rate ": """select [State/UT], sum(ltPercent) OverallLtR from (
                                    select [State/UT] , ((cast(Literate as float)/cast(Population as float))*100) as ltPercent
                                    from census_2011) x
                                    group by [State/UT]"""
    
}