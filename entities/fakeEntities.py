import random
import time
from datetime import datetime, timedelta
import statistics
from collections import Counter

# Generate realistic charging duration 
def generate_charging_duration():
    """
    Generate realistic charging duration in minutes based on historical data
    基于历史数据生成真实的充电时长（分钟）
    """
    duration = random.normalvariate(225.97, 146.09)  
    return max(1, min(672, int(duration)))  

# Calculate energy consumption 
def calculate_energy(duration_minutes):
    """
    Calculate energy consumption based on duration using your formula
    根据时长使用你的公式计算能耗
    """
    energy = 0.0557 * duration_minutes + 3.3513  
    energy = energy * random.uniform(0.9, 1.1) 
    return round(max(0, min(energy, 56.5)), 3)  

# Generate random time session 
def generate_random_session(session_number):
    """
    Generate a charging session with completely random start time
    生成完全随机开始时间的充电会话
    """
    
    # Basic session information 
    timestamp = int(time.time() * 1000)
    session_id = f"{session_number:03d}_{timestamp}"
    
    # Charging point selection 
    charging_point_prefixes = ["fakeStation-1-P-", "fakeStation-2-P-", "fakeStation-3-P-"]
    charging_point_prefix = random.choice(charging_point_prefixes)
    charging_point_id = f"{charging_point_prefix}{random.randint(1, 10):02d}"
    
    # Random time across the whole year 2024 
    base_time = datetime(2024, 1, 1, 0, 0, 0)
    start_offset = timedelta(
        days=random.randint(0, 364),    
        hours=random.randint(0, 23),    
        minutes=random.randint(0, 59),  
        seconds=random.randint(0, 59)   
    )
    start_time = base_time + start_offset
    
    # Generate charging duration and energy consumption 
    charging_duration = generate_charging_duration()  
    energy_consumed = calculate_energy(charging_duration)  
    
    # Calculate end time / 计算结束时间
    end_time = start_time + timedelta(minutes=charging_duration)
    
    # Build the NGSI-LD entity structure 
    entity = {
        "id": f"urn:ngsi-ld:ChargingSessionFake:session-{session_id}",
        "type": "ChargingSessionFake",
        
        "refChargingPoint": {
            "type": "Relationship",
            "object": f"urn:ngsi-ld:ChargingPoint:{charging_point_id}"
        },
        
        "sessionId": {
            "type": "Property",
            "value": session_id
        },
        
        "sessionStatus": {
            "type": "Property",
            "value": "ended"  # All sessions are completed 
        },
        
        "sessionStartTime": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "observedAt": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        },
        
        "sessionEndTime": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "observedAt": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        },
        
        "chargingDuration": {
            "type": "Property",
            "value": charging_duration,  # Duration in minutes 
            "unitCode": "MIN"
        },
        
        "energyConsumed": {
            "type": "Property",
            "value": energy_consumed,  # Energy consumption in kWh 
            "unitCode": "KWH"
        }
    }
    
    return entity

# Generate time slot distributed session 
def generate_time_slot_session(session_number):
    """
    Generate a charging session with time slot distribution
    生成按时间段分布的充电会话
    
    Time slots distribution 
    - morning (7:00-11:00): 20% 
    - daytime (11:00-18:00): 30% 
    - evening (18:00-22:00): 20% 
    - night (22:00-07:00): 30% 
    """
    
    # Basic session information 
    timestamp = int(time.time() * 1000)
    session_id = f"{session_number:03d}_{timestamp}"
    
    # Charging point selection 
    charging_point_prefixes = ["fakeStation-1-P-", "fakeStation-2-P-", "fakeStation-3-P-"]
    charging_point_prefix = random.choice(charging_point_prefixes)
    charging_point_id = f"{charging_point_prefix}{random.randint(1, 10):02d}"
    
    # Select time slot based on distribution / 根据分布选择时间段
    time_slots = ['morning', 'daytime', 'evening', 'night']
    weights = [20, 30, 20, 30]  # Corresponding percentages / 对应的百分比
    slot = random.choices(time_slots, weights=weights)[0]
    
    # Random date in 2024 
    base_time = datetime(2024, 1, 1, 0, 0, 0)
    random_date = base_time + timedelta(days=random.randint(0, 364))
    
    # Set start time based on time slot / 根据时间段设置开始时间
    if slot == 'morning':      # Morning: 7:00-11:00 
        hour = random.randint(7, 10)
    elif slot == 'daytime':    # Daytime: 11:00-18:00
        hour = random.randint(11, 17)
    elif slot == 'evening':    # Evening: 18:00-22:00 
        hour = random.randint(18, 21)
    else:  # night             # Night: 22:00-07:00 
        hour = random.choice(list(range(22, 24)) + list(range(0, 7)))
    
    start_time = random_date.replace(
        hour=hour,
        minute=random.randint(0, 59),
        second=random.randint(0, 59)
    )
    
    # Generate charging duration and energy consumption 
    charging_duration = generate_charging_duration()  
    energy_consumed = calculate_energy(charging_duration)  
    
    # Calculate end time 
    end_time = start_time + timedelta(minutes=charging_duration)
    
    # Build the NGSI-LD entity structure / 构建NGSI-LD实体结构
    entity = {
        "id": f"urn:ngsi-ld:ChargingSessionFake:session-{session_id}",
        "type": "ChargingSessionFake",
        
        "refChargingPoint": {
            "type": "Relationship",
            "object": f"urn:ngsi-ld:ChargingPoint:{charging_point_id}"
        },
        
        "sessionId": {
            "type": "Property",
            "value": session_id
        },
        
        "sessionStatus": {
            "type": "Property",
            "value": "ended"  # All sessions are completed 
        },
        
        "sessionStartTime": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "observedAt": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        },
        
        "sessionEndTime": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "observedAt": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        },
        
        "chargingDuration": {
            "type": "Property",
            "value": charging_duration,  # Duration in minutes 
            "unitCode": "MIN"
        },
        
        "energyConsumed": {
            "type": "Property",
            "value": energy_consumed,  # Energy consumption in kWh 
            "unitCode": "KWH"
        }
    }
    
    return entity

# Generate time informed distributed session 
def generate_informed_session(session_number):
    """
    Generate a charging session with informed user behavior
    生成知情用户行为的充电会话
    
    This version uses a weighted approach:
    - 60% chance of charging in encouraged hours (10:00-16:00) using normal distribution
    - 40% chance of charging at any other time uniformly
    这个版本使用加权方法：
    - 60%的概率在鼓励时间(10:00-16:00)使用正态分布充电
    - 40%的概率在其他任何时间均匀充电
    """
    
    # Basic session information 
    timestamp = int(time.time() * 1000)
    session_id = f"{session_number:03d}_{timestamp}"
    
    # Charging point selection 
    charging_point_prefixes = ["fakeStation-1-P-", "fakeStation-2-P-", "fakeStation-3-P-"]
    charging_point_prefix = random.choice(charging_point_prefixes)
    charging_point_id = f"{charging_point_prefix}{random.randint(1, 10):02d}"
    
    # Random date in 2024 
    base_time = datetime(2024, 1, 1, 0, 0, 0)
    random_date = base_time + timedelta(days=random.randint(0, 364))
    
    # Decide whether to follow encouragement or charge at any time
    # 决定是否遵循鼓励或在任何时间充电
    if random.random() < 0.6:  # 60% chance to follow encouragement
        # Generate time within encouraged hours using normal distribution
        # 使用正态分布在鼓励时间内生成时间
        # Center at 13:00, but constrain to 10:00-16:00 range
        while True:
            target_hour = random.normalvariate(13.0, 1.5)
            if 10 <= target_hour <= 16:
                hour = int(target_hour)
                break
    else:  # 40% chance to charge at any other time
        # Generate time outside encouraged hours or uniformly across all hours
        # 在鼓励时间外生成时间或在所有小时内均匀分布
        hour = random.randint(0, 23)
    
    # Generate minutes and seconds randomly
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    
    start_time = random_date.replace(
        hour=hour,
        minute=minute,
        second=second
    )
    
    # Generate charging duration and energy consumption 
    charging_duration = generate_charging_duration()  
    energy_consumed = calculate_energy(charging_duration)  
    
    # Calculate end time 
    end_time = start_time + timedelta(minutes=charging_duration)
    
    # Build the NGSI-LD entity structure 
    entity = {
        "id": f"urn:ngsi-ld:ChargingSessionFake:session-{session_id}",
        "type": "ChargingSessionFake",
        
        "refChargingPoint": {
            "type": "Relationship",
            "object": f"urn:ngsi-ld:ChargingPoint:{charging_point_id}"
        },
        
        "sessionId": {
            "type": "Property",
            "value": session_id
        },
        
        "sessionStatus": {
            "type": "Property",
            "value": "ended"  # All sessions are completed 
        },
        
        "sessionStartTime": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "observedAt": start_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        },
        
        "sessionEndTime": {
            "type": "Property",
            "value": {
                "@type": "DateTime",
                "@value": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
            },
            "observedAt": end_time.strftime("%Y-%m-%dT%H:%M:%S.000Z")
        },
        
        "chargingDuration": {
            "type": "Property",
            "value": charging_duration,  # Duration in minutes 
            "unitCode": "MIN"
        },
        
        "energyConsumed": {
            "type": "Property",
            "value": energy_consumed,  # Energy consumption in kWh 
            "unitCode": "KWH"
        }
    }
    
    return entity

# Generate a single type  
def generate_multiple_sessions(count=10, scenario="random"):
    """
    Generate multiple charging sessions with different scenarios
    生成多个不同场景的充电会话
    
    Args:
        count (int): Number of sessions to generate
        scenario (str): Type of scenario - "random", "slot", "informed"
    
    Returns:
        list: List of charging session entities
    """
    sessions = []
    
    # Validate scenario parameter
    valid_scenarios = ["random", "slot", "informed"]
    if scenario not in valid_scenarios:
        raise ValueError(f"Invalid scenario. Must be one of: {valid_scenarios}")
    
    for i in range(1, count + 1):
        # Small delay to ensure unique timestamps
        time.sleep(0.001)
        
        # Generate session based on selected scenario
        if scenario == "random":
            session = generate_random_session(i)
        elif scenario == "slot":
            session = generate_time_slot_session(i)
        elif scenario == "informed":
            session = generate_informed_session(i)
        
        sessions.append(session)
    
    return sessions

# Generate multiple types 
def generate_scenario_batch_sessions(total_count=30, batch_distribution=None):
    """
    Generate sessions in batches for each scenario
    为每个场景批量生成会话
    
    Args:
        total_count (int): Total number of sessions to generate
        batch_distribution (dict): Number of sessions for each scenario
                                 Default: equal distribution
    
    Returns:
        dict: Dictionary with scenario names as keys and session lists as values
    """
    if batch_distribution is None:
        # Equal distribution among three scenarios
        per_scenario = total_count // 3
        batch_distribution = {
            "random": per_scenario,
            "slot": per_scenario,
            "informed": total_count - (2 * per_scenario)  # Handle remainder
        }
    
    # Validate total count
    if sum(batch_distribution.values()) != total_count:
        raise ValueError("Batch distribution counts must sum to total_count")
    
    result = {}
    session_counter = 1
    
    for scenario, count in batch_distribution.items():
        sessions = []
        
        for i in range(count):
            # Small delay to ensure unique timestamps
            time.sleep(0.001)
            
            # Generate session based on scenario
            if scenario == "random":
                session = generate_random_session(session_counter)
            elif scenario == "slot":
                session = generate_time_slot_session(session_counter)
            elif scenario == "informed":
                session = generate_informed_session(session_counter)
            else:
                raise ValueError(f"Unknown scenario: {scenario}")
            
            sessions.append(session)
            session_counter += 1
        
        result[scenario] = sessions
    
    return result


#statistics tools
def show_enhanced_statistics(sessions):
    """
    Display comprehensive statistics of generated sessions
    显示生成会话的综合统计信息
    """
    if not sessions:
        print("No sessions to analyze")
        return
    
    # Extract basic data
    durations = [s['chargingDuration']['value'] for s in sessions]
    energies = [s['energyConsumed']['value'] for s in sessions]
    
    # Extract time information
    start_times = []
    charging_points = []
    
    for session in sessions:
        # Parse start time
        start_time_str = session['sessionStartTime']['value']['@value']
        start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
        start_times.append(start_time)
        
        # Extract charging point
        charging_point = session['refChargingPoint']['object'].split(':')[-1]
        charging_points.append(charging_point)
    
    # Extract hours from start times
    start_hours = [dt.hour for dt in start_times]
    start_days = [dt.strftime('%A') for dt in start_times]
    start_months = [dt.strftime('%B') for dt in start_times]
    
    print(f"CHARGING SESSIONS STATISTICS ({len(sessions)} sessions)")
    
    # BASIC STATISTICS
    print("\nDURATION STATISTICS (minutes)")
    print(f"Min: {min(durations):.1f}")
    print(f"Max: {max(durations):.1f}")
    print(f"Average: {statistics.mean(durations):.1f}")
    print(f"Median: {statistics.median(durations):.1f}")
    print(f"Std Dev: {statistics.stdev(durations):.1f}")
    
    # Duration distribution
    duration_ranges = {
        "< 1 hour": len([d for d in durations if d < 60]),
        "1-2 hours": len([d for d in durations if 60 <= d < 120]),
        "2-4 hours": len([d for d in durations if 120 <= d < 240]),
        "4-6 hours": len([d for d in durations if 240 <= d < 360]),
        "> 6 hours": len([d for d in durations if d >= 360])
    }
    
    print("\nDuration Distribution:")
    for range_name, count in duration_ranges.items():
        percentage = (count / len(sessions)) * 100
        print(f"{range_name}: {count} sessions ({percentage:.1f}%)")
    
    # ENERGY STATISTICS
    print("\nENERGY STATISTICS (kWh)")
    print(f"Min: {min(energies):.2f}")
    print(f"Max: {max(energies):.2f}")
    print(f"Average: {statistics.mean(energies):.2f}")
    print(f"Median: {statistics.median(energies):.2f}")
    print(f"Std Dev: {statistics.stdev(energies):.2f}")
    print(f"Total: {sum(energies):.2f}")
    
    # Energy distribution
    energy_ranges = {
        "< 5 kWh": len([e for e in energies if e < 5]),
        "5-10 kWh": len([e for e in energies if 5 <= e < 10]),
        "10-20 kWh": len([e for e in energies if 10 <= e < 20]),
        "20-30 kWh": len([e for e in energies if 20 <= e < 30]),
        "> 30 kWh": len([e for e in energies if e >= 30])
    }
    
    print("\nEnergy Distribution:")
    for range_name, count in energy_ranges.items():
        percentage = (count / len(sessions)) * 100
        print(f"{range_name}: {count} sessions ({percentage:.1f}%)")
    
    # TIME ANALYSIS
    print("\nTIME ANALYSIS")
    
    # Hourly distribution
    hour_counter = Counter(start_hours)
    print("Hourly Distribution (Top 5):")
    for hour, count in hour_counter.most_common(5):
        percentage = (count / len(sessions)) * 100
        print(f"{hour:02d}:00-{hour:02d}:59: {count} sessions ({percentage:.1f}%)")
    
    # Time period analysis
    time_periods = {
        "Night (00-06)": len([h for h in start_hours if 0 <= h <= 6]),
        "Morning (07-11)": len([h for h in start_hours if 7 <= h <= 11]),
        "Daytime (12-17)": len([h for h in start_hours if 12 <= h <= 17]),
        "Evening (18-23)": len([h for h in start_hours if 18 <= h <= 23])
    }
    
    print("\nTime Period Distribution:")
    for period, count in time_periods.items():
        percentage = (count / len(sessions)) * 100
        print(f"{period}: {count} sessions ({percentage:.1f}%)")
    
    # Day of week distribution
    day_counter = Counter(start_days)
    print("\nDay of Week Distribution:")
    for day, count in day_counter.most_common():
        percentage = (count / len(sessions)) * 100
        print(f"{day}: {count} sessions ({percentage:.1f}%)")
    
    # CHARGING INFRASTRUCTURE
    print("\nCHARGING INFRASTRUCTURE")
    
    # Charging point usage
    point_counter = Counter(charging_points)
    print(f"Charging Points Used: {len(point_counter)}")
    print("Top 5 Most Used Points:")
    for point, count in point_counter.most_common(5):
        percentage = (count / len(sessions)) * 100
        print(f"{point}: {count} sessions ({percentage:.1f}%)")
    
    # Station distribution
    stations = [cp.split('-P-')[0] for cp in charging_points]
    station_counter = Counter(stations)
    print("\nStation Distribution:")
    for station, count in station_counter.items():
        percentage = (count / len(sessions)) * 100
        print(f"{station}: {count} sessions ({percentage:.1f}%)")
    
    # TEMPORAL PATTERNS
    print("\nTEMPORAL PATTERNS")
    
    # Monthly distribution
    month_counter = Counter(start_months)
    print("Monthly Distribution (Top 5):")
    for month, count in month_counter.most_common(5):
        percentage = (count / len(sessions)) * 100
        print(f"{month}: {count} sessions ({percentage:.1f}%)")
    
    # Date range
    min_date = min(start_times).strftime('%Y-%m-%d')
    max_date = max(start_times).strftime('%Y-%m-%d')
    print(f"\nDate Range: {min_date} to {max_date}")
    
    # HISTORICAL COMPARISON
    print("\nHISTORICAL COMPARISON")
    historical_duration_avg = 225.97
    historical_duration_std = 146.09
    historical_energy_avg = 15.95
    
    generated_duration_avg = statistics.mean(durations)
    generated_energy_avg = statistics.mean(energies)
    
    duration_diff = generated_duration_avg - historical_duration_avg
    energy_diff = generated_energy_avg - historical_energy_avg
    
    print("Duration Average:")
    print(f"Historical: {historical_duration_avg:.1f} min")
    print(f"Generated: {generated_duration_avg:.1f} min")
    print(f"Difference: {duration_diff:+.1f} min ({(duration_diff/historical_duration_avg)*100:+.1f}%)")
    
    print("\nDuration Std Dev:")
    print(f"Historical: {historical_duration_std:.1f} min")
    print(f"Generated: {statistics.stdev(durations):.1f} min")
    
    print("\nEnergy Average:")
    print(f"Historical: {historical_energy_avg:.2f} kWh")
    print(f"Generated: {generated_energy_avg:.2f} kWh")
    print(f"Difference: {energy_diff:+.2f} kWh ({(energy_diff/historical_energy_avg)*100:+.1f}%)")
    
    # EFFICIENCY METRICS
    print("\nEFFICIENCY METRICS")
    
    # Energy per minute
    energy_per_minute = [e/d for e, d in zip(energies, durations)]
    print("Energy per Minute:")
    print(f"Average: {statistics.mean(energy_per_minute):.3f} kWh/min")
    print(f"Min: {min(energy_per_minute):.3f} kWh/min")
    print(f"Max: {max(energy_per_minute):.3f} kWh/min")
    
    # Sessions per charging point
    avg_sessions_per_point = len(sessions) / len(point_counter)
    print(f"\nAverage Sessions per Charging Point: {avg_sessions_per_point:.1f}")

def show_quick_statistics(sessions):
    """
    Display quick summary statistics (simplified version)
    显示快速摘要统计信息（简化版本）
    """
    if not sessions:
        print("No sessions to analyze")
        return
    
    durations = [s['chargingDuration']['value'] for s in sessions]
    energies = [s['energyConsumed']['value'] for s in sessions]
    
    print(f"Quick Stats ({len(sessions)} sessions)")
    print(f"Duration: {min(durations):.0f}-{max(durations):.0f} min (avg: {statistics.mean(durations):.1f})")
    print(f"Energy: {min(energies):.1f}-{max(energies):.1f} kWh (avg: {statistics.mean(energies):.2f})")
    print(f"Total Energy: {sum(energies):.1f} kWh")

def compare_scenarios(scenario_sessions_dict):
    """
    Compare statistics across different scenarios
    比较不同场景的统计信息
    
    Args:
        scenario_sessions_dict: Dictionary with scenario names as keys and session lists as values
    """
    print("SCENARIO COMPARISON")
    
    comparison_data = {}
    
    for scenario_name, sessions in scenario_sessions_dict.items():
        if not sessions:
            continue
            
        durations = [s['chargingDuration']['value'] for s in sessions]
        energies = [s['energyConsumed']['value'] for s in sessions]
        
        # Extract hours for time analysis
        start_hours = []
        for session in sessions:
            start_time_str = session['sessionStartTime']['value']['@value']
            start_time = datetime.fromisoformat(start_time_str.replace('Z', '+00:00'))
            start_hours.append(start_time.hour)
        
        comparison_data[scenario_name] = {
            'count': len(sessions),
            'duration_avg': statistics.mean(durations),
            'duration_std': statistics.stdev(durations),
            'energy_avg': statistics.mean(energies),
            'energy_std': statistics.stdev(energies),
            'peak_hour_at': max(set(start_hours), key=start_hours.count),
            'morning_sessions': len([h for h in start_hours if 7 <= h <= 11]),
            'daytime_sessions': len([h for h in start_hours if 12 <= h <= 17]),
            'evening_sessions': len([h for h in start_hours if 18 <= h <= 23])
        }
    
    # Display comparison table
    scenarios = list(comparison_data.keys())
    
    header = "Metric".ljust(20) + " " + " ".join(s.ljust(15) for s in scenarios)
    print(header)
    
    metrics = [
        ('Sessions', 'count', ''),
        ('Avg Duration (min)', 'duration_avg', '.1f'),
        ('Std Duration (min)', 'duration_std', '.1f'),
        ('Avg Energy (kWh)', 'energy_avg', '.2f'),
        ('Std Energy (kWh)', 'energy_std', '.2f'),
        ('Peak Hour At (hour)', 'peak_hour_at', ''),
        ('Morning (7-11)', 'morning_sessions', ''),
        ('Daytime (12-17)', 'daytime_sessions', ''),
        ('Evening (18-23)', 'evening_sessions', '')
    ]
    
    for metric_name, key, fmt in metrics:
        row = metric_name.ljust(20) + " "
        for scenario in scenarios:
            value = comparison_data[scenario][key]
            if fmt:
                formatted_value = f"{value:{fmt}}"
            else:
                formatted_value = str(value)
            row += formatted_value.ljust(15) + " "
        print(row)















