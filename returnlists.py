def return_all_features():
    all_features = ['diffcount', 'bpm', 'ranked_date',
       'difficultyrating', 'favourite_p', 'favourite_count', 'language',
       'genre', 'creator', 'playcount', 'passcount', 'successrate',
       'total_lengths', 'ar_in_order', 'cs_in_order', 'hp_in_order',
       'od_in_order', 'aim_difficulty', 'approach_rate_diff',
       'overall_difficulty', 'slider_factor', 'speed_difficulty',
       'speed_note_count', 'top_map_player', 'pp_value', 'max_v', 'mean_v',
       'max_x', 'min_t', 'mean_x', 'max_a', 'mean_a', 'max_rhythm_complexity',
       'max_angle', 'min_angle', 'mean_angle', '40-80 Hz', '80-250 Hz',
       '250-600 Hz', '600-4000 Hz', '4000-6000 Hz', '6000-8000 Hz',
       '8000-20000 Hz', 'Avg of IV 1', 'Avg of IV 2', 'Avg of IV 3',
       'Avg of IV 4', 'Avg of IV 5', 'Avg of IV 6', 'Avg of IV 7',
       'Avg of IV 8', 'Avg of IV 9', 'Avg of IV 10', '3 Percent of IV 1',
       '3 Percent of IV 2', '3 Percent of IV 3', '3 Percent of IV 4',
       '3 Percent of IV 5', '3 Percent of IV 6', '3 Percent of IV 7',
       '3 Percent of IV 8', '3 Percent of IV 9', '3 Percent of IV 10',
       '97 Percent of IV 1', '97 Percent of IV 2', '97 Percent of IV 3',
       '97 Percent of IV 4', '97 Percent of IV 5', '97 Percent of IV 6',
       '97 Percent of IV 7', '97 Percent of IV 8', '97 Percent of IV 9',
       '97 Percent of IV 10']
    
    return all_features

def return_website_features():
    website_features = ['diffcount', 'bpm', 'ranked_date',
    'difficultyrating', 'favourite_p', 'favourite_count', 'language',
    'genre', 'creator', 'playcount', 'passcount', 'successrate',
    'total_lengths', 'ar_in_order', 'cs_in_order', 'hp_in_order',
    'od_in_order', 'aim_difficulty', 'approach_rate_diff',   
    'overall_difficulty', 'slider_factor', 'speed_difficulty',
    'speed_note_count', 'top_map_player', 'pp_value']

    return website_features

def return_map_features():
    map_features = ['max_v', 'mean_v',
    'max_x', 'min_t', 'mean_x', 'max_a', 'mean_a', 'max_rhythm_complexity',
    'max_angle', 'min_angle', 'mean_angle']

    return map_features

def return_audio_features():
    audio_features = ['40-80 Hz', '80-250 Hz',
       '250-600 Hz', '600-4000 Hz', '4000-6000 Hz', '6000-8000 Hz',
       '8000-20000 Hz', 'Avg of IV 1', 'Avg of IV 2', 'Avg of IV 3',
       'Avg of IV 4', 'Avg of IV 5', 'Avg of IV 6', 'Avg of IV 7',
       'Avg of IV 8', 'Avg of IV 9', 'Avg of IV 10', '3 Percent of IV 1',
       '3 Percent of IV 2', '3 Percent of IV 3', '3 Percent of IV 4',
       '3 Percent of IV 5', '3 Percent of IV 6', '3 Percent of IV 7',
       '3 Percent of IV 8', '3 Percent of IV 9', '3 Percent of IV 10',
       '97 Percent of IV 1', '97 Percent of IV 2', '97 Percent of IV 3',
       '97 Percent of IV 4', '97 Percent of IV 5', '97 Percent of IV 6',
       '97 Percent of IV 7', '97 Percent of IV 8', '97 Percent of IV 9',
       '97 Percent of IV 10']

    return audio_features

def return_rl():
    rl_features = ['diffcount', 'bpm', 
       'difficultyrating', 'language',
       'genre', 'creator', 'successrate',
       'total_lengths', 'ar_in_order', 'cs_in_order', 'hp_in_order',
       'od_in_order', 'aim_difficulty', 'approach_rate_diff',
       'overall_difficulty', 'slider_factor', 'speed_difficulty',
       'speed_note_count', 'max_v', 'mean_v',
       'max_x', 'min_t', 'mean_x', 'max_a', 'mean_a', 'max_rhythm_complexity',
       'max_angle', 'min_angle', 'mean_angle', '40-80 Hz', '80-250 Hz',
       '250-600 Hz', '600-4000 Hz', '4000-6000 Hz', '6000-8000 Hz',
       '8000-20000 Hz', 'Avg of IV 1', 'Avg of IV 2', 'Avg of IV 3',
       'Avg of IV 4', 'Avg of IV 5', 'Avg of IV 6', 'Avg of IV 7',
       'Avg of IV 8', 'Avg of IV 9', 'Avg of IV 10', '3 Percent of IV 1',
       '3 Percent of IV 2', '3 Percent of IV 3', '3 Percent of IV 4',
       '3 Percent of IV 5', '3 Percent of IV 6', '3 Percent of IV 7',
       '3 Percent of IV 8', '3 Percent of IV 9', '3 Percent of IV 10',
       '97 Percent of IV 1', '97 Percent of IV 2', '97 Percent of IV 3',
       '97 Percent of IV 4', '97 Percent of IV 5', '97 Percent of IV 6',
       '97 Percent of IV 7', '97 Percent of IV 8', '97 Percent of IV 9',
       '97 Percent of IV 10']
    
    return rl_features

def return_rl2():
    rl_features = ['diffcount', 'bpm', 
       'difficultyrating', 'language',
       'genre', 'creator', 'successrate',
       'total_lengths', 'ar_in_order', 'cs_in_order', 'hp_in_order',
       'od_in_order', 'aim_difficulty', 'approach_rate_diff',
       'overall_difficulty', 'slider_factor', 'speed_difficulty',
       'speed_note_count', 'max_v', 'mean_v',
       'max_x', 'min_t', 'mean_x', 'max_a', 'mean_a', 'max_rhythm_complexity',
       'max_angle', 'min_angle', 'mean_angle', '40-80 Hz', '80-250 Hz',
       '250-600 Hz', '600-4000 Hz', '4000-6000 Hz', '6000-8000 Hz',
       '8000-20000 Hz']
    
    return rl_features