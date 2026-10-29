# Data dictionary
Every CSV is synthetic. Metadata fields mean: `synthetic` = true; `source_type` = synthetic; `generated_at` = generation timestamp; `generation_method` = seeded simulation; `source_reference` = blank; `real_source_type` identifies only the normal real-source category.
## data/vehicles/vehicles.csv
Rows: 12. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| manufacturer | string or numeric | Synthetic `manufacturer` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| model | string or numeric | Synthetic `model` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| variant | string or numeric | Synthetic `variant` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_category | string or numeric | Synthetic `vehicle_category` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| body_type | string or numeric | Synthetic `body_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| launch_year | string or numeric | Synthetic `launch_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| model_year | string or numeric | Synthetic `model_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ex_showroom_price | string or numeric | Synthetic `ex_showroom_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_on_road_price | string or numeric | Synthetic `estimated_on_road_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| motor_type | string or numeric | Synthetic `motor_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| motor_power_kw | string or numeric | Synthetic `motor_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| motor_power_bhp | string or numeric | Synthetic `motor_power_bhp` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| torque_nm | string or numeric | Synthetic `torque_nm` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| drive_type | string or numeric | Synthetic `drive_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| kerb_weight_kg | string or numeric | Synthetic `kerb_weight_kg` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| length_mm | string or numeric | Synthetic `length_mm` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| width_mm | string or numeric | Synthetic `width_mm` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| height_mm | string or numeric | Synthetic `height_mm` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| wheelbase_mm | string or numeric | Synthetic `wheelbase_mm` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ground_clearance_mm | string or numeric | Synthetic `ground_clearance_mm` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| boot_capacity_l | string or numeric | Synthetic `boot_capacity_l` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| seating_capacity | string or numeric | Synthetic `seating_capacity` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| top_speed_kmph | string or numeric | Synthetic `top_speed_kmph` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| acceleration_0_100_sec | string or numeric | Synthetic `acceleration_0_100_sec` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| claimed_range_km | string or numeric | Synthetic `claimed_range_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_range_km | string or numeric | Synthetic `city_range_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_range_km | string or numeric | Synthetic `highway_range_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| mixed_real_world_range_km | string or numeric | Synthetic `mixed_real_world_range_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| efficiency_kwh_per_100km | string or numeric | Synthetic `efficiency_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| warranty_years | string or numeric | Synthetic `warranty_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| warranty_km | string or numeric | Synthetic `warranty_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_years | string or numeric | Synthetic `battery_warranty_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_km | string or numeric | Synthetic `battery_warranty_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| safety_features | string or numeric | Synthetic `safety_features` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| adas_level | string or numeric | Synthetic `adas_level` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| infotainment_features | string or numeric | Synthetic `infotainment_features` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| connected_features | string or numeric | Synthetic `connected_features` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/vehicles/batteries.csv
Rows: 12. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| battery_id | string or numeric | Synthetic `battery_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_capacity_kwh | string or numeric | Synthetic `battery_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| usable_capacity_kwh | string or numeric | Synthetic `usable_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| chemistry | string or numeric | Synthetic `chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| cell_format | string or numeric | Synthetic `cell_format` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| nominal_voltage | string or numeric | Synthetic `nominal_voltage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_density_wh_kg | string or numeric | Synthetic `energy_density_wh_kg` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_weight_kg | string or numeric | Synthetic `battery_weight_kg` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_management | string or numeric | Synthetic `thermal_management` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| cooling_type | string or numeric | Synthetic `cooling_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| manufacturer_if_known | string or numeric | Synthetic `manufacturer_if_known` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_years | string or numeric | Synthetic `battery_warranty_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_km | string or numeric | Synthetic `battery_warranty_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| max_ac_power_kw | string or numeric | Synthetic `max_ac_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| max_dc_power_kw | string or numeric | Synthetic `max_dc_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_10_80_minutes | string or numeric | Synthetic `charging_10_80_minutes` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_20_80_minutes | string or numeric | Synthetic `charging_20_80_minutes` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| recommended_soc_range | string or numeric | Synthetic `recommended_soc_range` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charging_supported | string or numeric | Synthetic `fast_charging_supported` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| v2l_supported | string or numeric | Synthetic `v2l_supported` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_pack_architecture | string or numeric | Synthetic `battery_pack_architecture` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/battery/soh_dataset.csv
Rows: 24000. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| observation_id | string or numeric | Synthetic `observation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_instance_id | string or numeric | Synthetic `battery_instance_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_chemistry | string or numeric | Synthetic `battery_chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_months | string or numeric | Synthetic `vehicle_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature_c | string or numeric | Synthetic `average_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_soc_percent | string or numeric | Synthetic `average_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_soc_percent | string or numeric | Synthetic `minimum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_soc_percent | string or numeric | Synthetic `maximum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_depth_of_discharge | string or numeric | Synthetic `average_depth_of_discharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cycles | string or numeric | Synthetic `charging_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_cycles | string or numeric | Synthetic `fast_charge_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_percentage | string or numeric | Synthetic `fast_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| slow_charge_percentage | string or numeric | Synthetic `slow_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_charge_power_kw | string or numeric | Synthetic `average_charge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_discharge_power_kw | string or numeric | Synthetic `average_discharge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance_km | string or numeric | Synthetic `daily_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance_km | string or numeric | Synthetic `monthly_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage_percentage | string or numeric | Synthetic `highway_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_usage_percentage | string or numeric | Synthetic `city_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_consumption_kwh_per_100km | string or numeric | Synthetic `energy_consumption_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_high_soc_hours | string or numeric | Synthetic `time_at_high_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_low_soc_hours | string or numeric | Synthetic `time_at_low_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_events | string or numeric | Synthetic `thermal_events` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calendar_age_months | string or numeric | Synthetic `calendar_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_capacity_kwh | string or numeric | Synthetic `estimated_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention_percent | string or numeric | Synthetic `capacity_retention_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| degradation_rate_percent_per_year | string or numeric | Synthetic `degradation_rate_percent_per_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| remaining_useful_life_months | string or numeric | Synthetic `remaining_useful_life_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/battery/degradation_dataset.csv
Rows: 24000. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| observation_id | string or numeric | Synthetic `observation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_instance_id | string or numeric | Synthetic `battery_instance_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_chemistry | string or numeric | Synthetic `battery_chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_months | string or numeric | Synthetic `vehicle_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature_c | string or numeric | Synthetic `average_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_soc_percent | string or numeric | Synthetic `average_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_soc_percent | string or numeric | Synthetic `minimum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_soc_percent | string or numeric | Synthetic `maximum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_depth_of_discharge | string or numeric | Synthetic `average_depth_of_discharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cycles | string or numeric | Synthetic `charging_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_cycles | string or numeric | Synthetic `fast_charge_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_percentage | string or numeric | Synthetic `fast_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| slow_charge_percentage | string or numeric | Synthetic `slow_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_charge_power_kw | string or numeric | Synthetic `average_charge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_discharge_power_kw | string or numeric | Synthetic `average_discharge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance_km | string or numeric | Synthetic `daily_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance_km | string or numeric | Synthetic `monthly_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage_percentage | string or numeric | Synthetic `highway_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_usage_percentage | string or numeric | Synthetic `city_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_consumption_kwh_per_100km | string or numeric | Synthetic `energy_consumption_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_high_soc_hours | string or numeric | Synthetic `time_at_high_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_low_soc_hours | string or numeric | Synthetic `time_at_low_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_events | string or numeric | Synthetic `thermal_events` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calendar_age_months | string or numeric | Synthetic `calendar_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_capacity_kwh | string or numeric | Synthetic `estimated_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention_percent | string or numeric | Synthetic `capacity_retention_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| degradation_rate_percent_per_year | string or numeric | Synthetic `degradation_rate_percent_per_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| remaining_useful_life_months | string or numeric | Synthetic `remaining_useful_life_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/ml/train.csv
Rows: 14400. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| observation_id | string or numeric | Synthetic `observation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_instance_id | string or numeric | Synthetic `battery_instance_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_chemistry | string or numeric | Synthetic `battery_chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_months | string or numeric | Synthetic `vehicle_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature_c | string or numeric | Synthetic `average_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_soc_percent | string or numeric | Synthetic `average_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_soc_percent | string or numeric | Synthetic `minimum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_soc_percent | string or numeric | Synthetic `maximum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_depth_of_discharge | string or numeric | Synthetic `average_depth_of_discharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cycles | string or numeric | Synthetic `charging_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_cycles | string or numeric | Synthetic `fast_charge_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_percentage | string or numeric | Synthetic `fast_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| slow_charge_percentage | string or numeric | Synthetic `slow_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_charge_power_kw | string or numeric | Synthetic `average_charge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_discharge_power_kw | string or numeric | Synthetic `average_discharge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance_km | string or numeric | Synthetic `daily_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance_km | string or numeric | Synthetic `monthly_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage_percentage | string or numeric | Synthetic `highway_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_usage_percentage | string or numeric | Synthetic `city_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_consumption_kwh_per_100km | string or numeric | Synthetic `energy_consumption_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_high_soc_hours | string or numeric | Synthetic `time_at_high_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_low_soc_hours | string or numeric | Synthetic `time_at_low_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_events | string or numeric | Synthetic `thermal_events` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calendar_age_months | string or numeric | Synthetic `calendar_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_capacity_kwh | string or numeric | Synthetic `estimated_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention_percent | string or numeric | Synthetic `capacity_retention_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| degradation_rate_percent_per_year | string or numeric | Synthetic `degradation_rate_percent_per_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| remaining_useful_life_months | string or numeric | Synthetic `remaining_useful_life_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/ml/validation.csv
Rows: 4800. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| observation_id | string or numeric | Synthetic `observation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_instance_id | string or numeric | Synthetic `battery_instance_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_chemistry | string or numeric | Synthetic `battery_chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_months | string or numeric | Synthetic `vehicle_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature_c | string or numeric | Synthetic `average_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_soc_percent | string or numeric | Synthetic `average_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_soc_percent | string or numeric | Synthetic `minimum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_soc_percent | string or numeric | Synthetic `maximum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_depth_of_discharge | string or numeric | Synthetic `average_depth_of_discharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cycles | string or numeric | Synthetic `charging_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_cycles | string or numeric | Synthetic `fast_charge_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_percentage | string or numeric | Synthetic `fast_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| slow_charge_percentage | string or numeric | Synthetic `slow_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_charge_power_kw | string or numeric | Synthetic `average_charge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_discharge_power_kw | string or numeric | Synthetic `average_discharge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance_km | string or numeric | Synthetic `daily_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance_km | string or numeric | Synthetic `monthly_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage_percentage | string or numeric | Synthetic `highway_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_usage_percentage | string or numeric | Synthetic `city_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_consumption_kwh_per_100km | string or numeric | Synthetic `energy_consumption_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_high_soc_hours | string or numeric | Synthetic `time_at_high_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_low_soc_hours | string or numeric | Synthetic `time_at_low_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_events | string or numeric | Synthetic `thermal_events` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calendar_age_months | string or numeric | Synthetic `calendar_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_capacity_kwh | string or numeric | Synthetic `estimated_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention_percent | string or numeric | Synthetic `capacity_retention_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| degradation_rate_percent_per_year | string or numeric | Synthetic `degradation_rate_percent_per_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| remaining_useful_life_months | string or numeric | Synthetic `remaining_useful_life_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/ml/test.csv
Rows: 4800. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| observation_id | string or numeric | Synthetic `observation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_instance_id | string or numeric | Synthetic `battery_instance_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_chemistry | string or numeric | Synthetic `battery_chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_months | string or numeric | Synthetic `vehicle_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature_c | string or numeric | Synthetic `average_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_soc_percent | string or numeric | Synthetic `average_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_soc_percent | string or numeric | Synthetic `minimum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_soc_percent | string or numeric | Synthetic `maximum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_depth_of_discharge | string or numeric | Synthetic `average_depth_of_discharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cycles | string or numeric | Synthetic `charging_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_cycles | string or numeric | Synthetic `fast_charge_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_percentage | string or numeric | Synthetic `fast_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| slow_charge_percentage | string or numeric | Synthetic `slow_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_charge_power_kw | string or numeric | Synthetic `average_charge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_discharge_power_kw | string or numeric | Synthetic `average_discharge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance_km | string or numeric | Synthetic `daily_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance_km | string or numeric | Synthetic `monthly_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage_percentage | string or numeric | Synthetic `highway_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_usage_percentage | string or numeric | Synthetic `city_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_consumption_kwh_per_100km | string or numeric | Synthetic `energy_consumption_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_high_soc_hours | string or numeric | Synthetic `time_at_high_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_low_soc_hours | string or numeric | Synthetic `time_at_low_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_events | string or numeric | Synthetic `thermal_events` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calendar_age_months | string or numeric | Synthetic `calendar_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_capacity_kwh | string or numeric | Synthetic `estimated_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention_percent | string or numeric | Synthetic `capacity_retention_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| degradation_rate_percent_per_year | string or numeric | Synthetic `degradation_rate_percent_per_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| remaining_useful_life_months | string or numeric | Synthetic `remaining_useful_life_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/ml/ood_test.csv
Rows: 2000. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| observation_id | string or numeric | Synthetic `observation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_instance_id | string or numeric | Synthetic `battery_instance_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_chemistry | string or numeric | Synthetic `battery_chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_months | string or numeric | Synthetic `vehicle_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature_c | string or numeric | Synthetic `average_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_soc_percent | string or numeric | Synthetic `average_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_soc_percent | string or numeric | Synthetic `minimum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_soc_percent | string or numeric | Synthetic `maximum_soc_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_depth_of_discharge | string or numeric | Synthetic `average_depth_of_discharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cycles | string or numeric | Synthetic `charging_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_cycles | string or numeric | Synthetic `fast_charge_cycles` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge_percentage | string or numeric | Synthetic `fast_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| slow_charge_percentage | string or numeric | Synthetic `slow_charge_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_charge_power_kw | string or numeric | Synthetic `average_charge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_discharge_power_kw | string or numeric | Synthetic `average_discharge_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance_km | string or numeric | Synthetic `daily_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance_km | string or numeric | Synthetic `monthly_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage_percentage | string or numeric | Synthetic `highway_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_usage_percentage | string or numeric | Synthetic `city_usage_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_consumption_kwh_per_100km | string or numeric | Synthetic `energy_consumption_kwh_per_100km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_high_soc_hours | string or numeric | Synthetic `time_at_high_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| time_at_low_soc_hours | string or numeric | Synthetic `time_at_low_soc_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| thermal_events | string or numeric | Synthetic `thermal_events` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calendar_age_months | string or numeric | Synthetic `calendar_age_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_capacity_kwh | string or numeric | Synthetic `estimated_capacity_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention_percent | string or numeric | Synthetic `capacity_retention_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| degradation_rate_percent_per_year | string or numeric | Synthetic `degradation_rate_percent_per_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| remaining_useful_life_months | string or numeric | Synthetic `remaining_useful_life_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/charging/charging_sessions.csv
Rows: 5000. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| session_id | string or numeric | Synthetic `session_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| timestamp | string or numeric | Synthetic `timestamp` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| start_soc | string or numeric | Synthetic `start_soc` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| end_soc | string or numeric | Synthetic `end_soc` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_delivered_kwh | string or numeric | Synthetic `energy_delivered_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_type | string or numeric | Synthetic `charging_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charger_power_kw | string or numeric | Synthetic `charger_power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| duration_minutes | string or numeric | Synthetic `duration_minutes` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| location_type | string or numeric | Synthetic `location_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charge | string or numeric | Synthetic `fast_charge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cost | string or numeric | Synthetic `charging_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_temperature_c | string or numeric | Synthetic `battery_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_efficiency | string or numeric | Synthetic `charging_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| session_success | string or numeric | Synthetic `session_success` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| interruption_reason | string or numeric | Synthetic `interruption_reason` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/battery/range_trips.csv
Rows: 5000. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| trip_id | string or numeric | Synthetic `trip_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| date | string or numeric | Synthetic `date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| distance_km | string or numeric | Synthetic `distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| starting_soc | string or numeric | Synthetic `starting_soc` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ending_soc | string or numeric | Synthetic `ending_soc` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_used_kwh | string or numeric | Synthetic `energy_used_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_speed_kmph | string or numeric | Synthetic `average_speed_kmph` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_speed_kmph | string or numeric | Synthetic `maximum_speed_kmph` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ambient_temperature_c | string or numeric | Synthetic `ambient_temperature_c` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| traffic_level | string or numeric | Synthetic `traffic_level` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| road_type | string or numeric | Synthetic `road_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city_highway_ratio | string or numeric | Synthetic `city_highway_ratio` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| occupancy | string or numeric | Synthetic `occupancy` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| air_conditioning_used | string or numeric | Synthetic `air_conditioning_used` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| tyre_pressure_condition | string or numeric | Synthetic `tyre_pressure_condition` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| driving_style | string or numeric | Synthetic `driving_style` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| rain | string or numeric | Synthetic `rain` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| elevation_change_m | string or numeric | Synthetic `elevation_change_m` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| calculated_efficiency | string or numeric | Synthetic `calculated_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| estimated_range_km | string or numeric | Synthetic `estimated_range_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/charging/charging_stations.csv
Rows: 40. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| station_id | string or numeric | Synthetic `station_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| operator | string or numeric | Synthetic `operator` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| state | string or numeric | Synthetic `state` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city | string or numeric | Synthetic `city` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| latitude | string or numeric | Synthetic `latitude` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| longitude | string or numeric | Synthetic `longitude` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| station_type | string or numeric | Synthetic `station_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charger_type | string or numeric | Synthetic `charger_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| connector_type | string or numeric | Synthetic `connector_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| power_kw | string or numeric | Synthetic `power_kw` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| number_of_ports | string or numeric | Synthetic `number_of_ports` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| availability | string or numeric | Synthetic `availability` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| operating_hours | string or numeric | Synthetic `operating_hours` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| price_per_kwh | string or numeric | Synthetic `price_per_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| price_per_minute | string or numeric | Synthetic `price_per_minute` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| payment_methods | string or numeric | Synthetic `payment_methods` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| network_status | string or numeric | Synthetic `network_status` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| installation_year | string or numeric | Synthetic `installation_year` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/economics/electricity_tariffs.csv
Rows: 8. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| tariff_id | string or numeric | Synthetic `tariff_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| state | string or numeric | Synthetic `state` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| discom | string or numeric | Synthetic `discom` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| consumer_category | string or numeric | Synthetic `consumer_category` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fixed_charge | string or numeric | Synthetic `fixed_charge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_charge_per_kwh | string or numeric | Synthetic `energy_charge_per_kwh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| tod_peak_rate | string or numeric | Synthetic `tod_peak_rate` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| tod_offpeak_rate | string or numeric | Synthetic `tod_offpeak_rate` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ev_specific_rate | string or numeric | Synthetic `ev_specific_rate` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| taxes | string or numeric | Synthetic `taxes` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| surcharge | string or numeric | Synthetic `surcharge` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| effective_from | string or numeric | Synthetic `effective_from` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| effective_until | string or numeric | Synthetic `effective_until` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/market/climate.csv
Rows: 96. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| city | string or numeric | Synthetic `city` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| state | string or numeric | Synthetic `state` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| month | string or numeric | Synthetic `month` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| average_temperature | string or numeric | Synthetic `average_temperature` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| minimum_temperature | string or numeric | Synthetic `minimum_temperature` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maximum_temperature | string or numeric | Synthetic `maximum_temperature` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| humidity | string or numeric | Synthetic `humidity` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| rainfall | string or numeric | Synthetic `rainfall` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| extreme_temperature_days | string or numeric | Synthetic `extreme_temperature_days` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/market/registrations.csv
Rows: 288. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| month | string or numeric | Synthetic `month` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| state | string or numeric | Synthetic `state` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city | string or numeric | Synthetic `city` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| manufacturer | string or numeric | Synthetic `manufacturer` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_category | string or numeric | Synthetic `vehicle_category` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| registrations | string or numeric | Synthetic `registrations` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| market_share | string or numeric | Synthetic `market_share` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| year_on_year_growth | string or numeric | Synthetic `year_on_year_growth` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/policies/schemes.csv
Rows: 13. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| policy_id | string or numeric | Synthetic `policy_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| policy_name | string or numeric | Synthetic `policy_name` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| jurisdiction | string or numeric | Synthetic `jurisdiction` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| state | string or numeric | Synthetic `state` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_category | string or numeric | Synthetic `vehicle_category` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| eligible_vehicle | string or numeric | Synthetic `eligible_vehicle` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| eligibility_conditions | string or numeric | Synthetic `eligibility_conditions` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| incentive_type | string or numeric | Synthetic `incentive_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| incentive_amount | string or numeric | Synthetic `incentive_amount` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_capacity_condition | string or numeric | Synthetic `battery_capacity_condition` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_price_condition | string or numeric | Synthetic `vehicle_price_condition` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| income_condition | string or numeric | Synthetic `income_condition` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| registration_condition | string or numeric | Synthetic `registration_condition` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| start_date | string or numeric | Synthetic `start_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| end_date | string or numeric | Synthetic `end_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| application_process | string or numeric | Synthetic `application_process` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| document_requirements | string or numeric | Synthetic `document_requirements` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| status | string or numeric | Synthetic `status` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| last_verified | string or numeric | Synthetic `last_verified` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| official_source_url | string or numeric | Synthetic `official_source_url` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/policies/regulations.csv
Rows: 12. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| regulation_id | string or numeric | Synthetic `regulation_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| title | string or numeric | Synthetic `title` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| jurisdiction | string or numeric | Synthetic `jurisdiction` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| category | string or numeric | Synthetic `category` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| effective_date | string or numeric | Synthetic `effective_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| expiry_date | string or numeric | Synthetic `expiry_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| summary | string or numeric | Synthetic `summary` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| requirements | string or numeric | Synthetic `requirements` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| applicability | string or numeric | Synthetic `applicability` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| document_version | string or numeric | Synthetic `document_version` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| last_updated | string or numeric | Synthetic `last_updated` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/policies/manufacturer_policies.csv
Rows: 12. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| manufacturer | string or numeric | Synthetic `manufacturer` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| basic_warranty_years | string or numeric | Synthetic `basic_warranty_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| basic_warranty_km | string or numeric | Synthetic `basic_warranty_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_years | string or numeric | Synthetic `battery_warranty_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_km | string or numeric | Synthetic `battery_warranty_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_warranty_soh_threshold | string or numeric | Synthetic `battery_warranty_soh_threshold` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| roadside_assistance | string or numeric | Synthetic `roadside_assistance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| service_interval_km | string or numeric | Synthetic `service_interval_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| service_interval_months | string or numeric | Synthetic `service_interval_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| warranty_exclusions | string or numeric | Synthetic `warranty_exclusions` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| extended_warranty | string or numeric | Synthetic `extended_warranty` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| software_support_years | string or numeric | Synthetic `software_support_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_replacement_policy | string or numeric | Synthetic `battery_replacement_policy` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/economics/tco_inputs.csv
Rows: 48. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ownership_years | string or numeric | Synthetic `ownership_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| purchase_price | string or numeric | Synthetic `purchase_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| subsidy | string or numeric | Synthetic `subsidy` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| registration_cost | string or numeric | Synthetic `registration_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| insurance_annual | string or numeric | Synthetic `insurance_annual` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| home_charger_cost | string or numeric | Synthetic `home_charger_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charger_installation_cost | string or numeric | Synthetic `charger_installation_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| annual_distance_km | string or numeric | Synthetic `annual_distance_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| electricity_price | string or numeric | Synthetic `electricity_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| public_charging_percentage | string or numeric | Synthetic `public_charging_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| public_charging_price | string or numeric | Synthetic `public_charging_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| home_charging_price | string or numeric | Synthetic `home_charging_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| energy_efficiency | string or numeric | Synthetic `energy_efficiency` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_losses | string or numeric | Synthetic `charging_losses` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| annual_maintenance | string or numeric | Synthetic `annual_maintenance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| annual_tyre_cost | string or numeric | Synthetic `annual_tyre_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| annual_insurance | string or numeric | Synthetic `annual_insurance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| financing_rate | string or numeric | Synthetic `financing_rate` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| loan_period | string or numeric | Synthetic `loan_period` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| expected_resale_percentage | string or numeric | Synthetic `expected_resale_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| purchase_cost | string or numeric | Synthetic `purchase_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| running_cost | string or numeric | Synthetic `running_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_cost | string or numeric | Synthetic `charging_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| maintenance_cost | string or numeric | Synthetic `maintenance_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| insurance | string or numeric | Synthetic `insurance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| financing | string or numeric | Synthetic `financing` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| depreciation | string or numeric | Synthetic `depreciation` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| resale_value | string or numeric | Synthetic `resale_value` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| total_ownership_cost | string or numeric | Synthetic `total_ownership_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| cost_per_km | string or numeric | Synthetic `cost_per_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_ownership_cost | string or numeric | Synthetic `monthly_ownership_cost` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/economics/resale_market.csv
Rows: 96. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_age_years | string or numeric | Synthetic `vehicle_age_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh_percent | string or numeric | Synthetic `soh_percent` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| warranty_remaining_months | string or numeric | Synthetic `warranty_remaining_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| condition | string or numeric | Synthetic `condition` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| accident_history | string or numeric | Synthetic `accident_history` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| service_history | string or numeric | Synthetic `service_history` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| location | string or numeric | Synthetic `location` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| original_price | string or numeric | Synthetic `original_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| used_market_price | string or numeric | Synthetic `used_market_price` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| market_demand_index | string or numeric | Synthetic `market_demand_index` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| resale_percentage | string or numeric | Synthetic `resale_percentage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/reviews/owner_reviews.csv
Rows: 144. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| review_id | string or numeric | Synthetic `review_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| review_date | string or numeric | Synthetic `review_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ownership_months | string or numeric | Synthetic `ownership_months` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| odometer_km | string or numeric | Synthetic `odometer_km` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| rating | string or numeric | Synthetic `rating` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| range_experience | string or numeric | Synthetic `range_experience` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charging_experience | string or numeric | Synthetic `charging_experience` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| service_experience | string or numeric | Synthetic `service_experience` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_experience | string or numeric | Synthetic `battery_experience` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| software_experience | string or numeric | Synthetic `software_experience` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| comfort | string or numeric | Synthetic `comfort` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| reliability | string or numeric | Synthetic `reliability` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| pros | string or numeric | Synthetic `pros` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| cons | string or numeric | Synthetic `cons` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| complaint_category | string or numeric | Synthetic `complaint_category` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| sentiment | string or numeric | Synthetic `sentiment` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| severity | string or numeric | Synthetic `severity` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/safety/safety_events.csv
Rows: 4. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| event_id | string or numeric | Synthetic `event_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| vehicle_id | string or numeric | Synthetic `vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| event_type | string or numeric | Synthetic `event_type` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| component | string or numeric | Synthetic `component` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| severity | string or numeric | Synthetic `severity` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| date | string or numeric | Synthetic `date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| affected_units | string or numeric | Synthetic `affected_units` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| description | string or numeric | Synthetic `description` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| resolution | string or numeric | Synthetic `resolution` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| status | string or numeric | Synthetic `status` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| officially_confirmed | string or numeric | Synthetic `officially_confirmed` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/users/user_profiles.csv
Rows: 100. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| user_id | string or numeric | Synthetic `user_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| budget | string or numeric | Synthetic `budget` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| monthly_distance | string or numeric | Synthetic `monthly_distance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| daily_distance | string or numeric | Synthetic `daily_distance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| city | string or numeric | Synthetic `city` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| state | string or numeric | Synthetic `state` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| home_charging | string or numeric | Synthetic `home_charging` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| workplace_charging | string or numeric | Synthetic `workplace_charging` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| highway_usage | string or numeric | Synthetic `highway_usage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| preferred_range | string or numeric | Synthetic `preferred_range` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| performance_priority | string or numeric | Synthetic `performance_priority` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| safety_priority | string or numeric | Synthetic `safety_priority` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| comfort_priority | string or numeric | Synthetic `comfort_priority` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| low_running_cost_priority | string or numeric | Synthetic `low_running_cost_priority` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| fast_charging_priority | string or numeric | Synthetic `fast_charging_priority` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| battery_longevity_priority | string or numeric | Synthetic `battery_longevity_priority` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| ownership_years | string or numeric | Synthetic `ownership_years` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| family_size | string or numeric | Synthetic `family_size` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| recommendation_target_vehicle_id | string or numeric | Synthetic `recommendation_target_vehicle_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/battery/experimental_cells.csv
Rows: 120. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| cell_id | string or numeric | Synthetic `cell_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| chemistry | string or numeric | Synthetic `chemistry` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| cycle_number | string or numeric | Synthetic `cycle_number` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| temperature | string or numeric | Synthetic `temperature` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charge_current | string or numeric | Synthetic `charge_current` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| discharge_current | string or numeric | Synthetic `discharge_current` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| charge_capacity | string or numeric | Synthetic `charge_capacity` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| discharge_capacity | string or numeric | Synthetic `discharge_capacity` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| internal_resistance | string or numeric | Synthetic `internal_resistance` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| voltage | string or numeric | Synthetic `voltage` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| capacity_retention | string or numeric | Synthetic `capacity_retention` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| soh | string or numeric | Synthetic `soh` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
## data/sources/source_metadata.csv
Rows: 1. Reference class: `reference_only`.
| column_name | data_type | description | unit | allowed_values | nullable | example | generation_logic |
|---|---|---|---|---|---|---|---|
| source_id | string or numeric | Synthetic `source_id` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| source_name | string or numeric | Synthetic `source_name` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| source_type | string or numeric | Synthetic `source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| organization | string or numeric | Synthetic `organization` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| url | string or numeric | Synthetic `url` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| document_title | string or numeric | Synthetic `document_title` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| publication_date | string or numeric | Synthetic `publication_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| collection_date | string or numeric | Synthetic `collection_date` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| last_verified | string or numeric | Synthetic `last_verified` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| valid_from | string or numeric | Synthetic `valid_from` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| valid_until | string or numeric | Synthetic `valid_until` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| reliability_level | string or numeric | Synthetic `reliability_level` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| data_categories | string or numeric | Synthetic `data_categories` field | varies | synthetic valid values | yes where applicable | synthetic value | seeded rule based simulation |
| synthetic | string or numeric | Synthetic `synthetic` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generated_at | string or numeric | Synthetic `generated_at` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| generation_method | string or numeric | Synthetic `generation_method` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| source_reference | string or numeric | Synthetic `source_reference` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
| real_source_type | string or numeric | Synthetic `real_source_type` field | varies | synthetic valid values | yes where applicable | metadata | seeded rule based simulation |
