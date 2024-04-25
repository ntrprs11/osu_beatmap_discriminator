# osu v1.0



## What is osu?

[osu!](https://osu.ppy.sh/home) is a free-to-play rhythm game created and developed by Dean "peppy" Herbert. It was first released on 16 September 2007 and was inspired by the old rhythm game Osu! Tatakae! Ouendan and osu! is primarly written in C# and [Open-source](https://github.com/ppy/osu).

## osu! map folder and its structure.

An osu! map folder requires at least 3 files to count as a rankable osu! map.
An audio file, a background file (picture or video) and a .osu file for the difficulty its representing in the mapset.
Optionally there can be multiple .osu for multiple difficultys in the set and in other osu! modes. There are also "Hitsounds which are optional for gameplay purposes that are named like soft_whistle.mp3 (these get removed in the preprocessing) and lastly there's the option to implement a storyboard (.osb file) which is an animated background for story telling.

## What is the project supposed to do?

The project uses all kind of data from osu! Beatmaps to predict the actual Userratings in a different set of Maps, however in order for it to have a real life application some of the used features must be removed / changed.

## How to use this project?

- [ ] Fork / Clone the Project
- [ ] Create 2 Folders in the repository one named "data" the other one "input". data will be used for the trainingsdata and input will be used for our input (prediction).
- [ ] It's important to have an [osu! account](https://osu.ppy.sh/home/download), which only can be created ingame after downloading osu! in the first place (Yeah osu! isn't very known for accessability).
- [ ] Once the Account has been created an OAuth Application has to be created. Go to your Profile -> Settings -> "New OAuth Application" -> Enter a Application Name -> Register application.
- [ ] Once the OAuth Application has been created you need to create a ".env" file where you add these lines (replace 'client_x' with the actual information from the application):
client_id='client_id'
client_secret='client_secret'
- [ ] Install all missing librarys "pip install -r requirements.txt", if there are any Errors try different versions of each library / manually install missing librarys.
- [ ] Move all osu! map folders you want to use as trainingsdata into the "data" folder and all input maps into "input", it's very important that every map is in a ranked state right now! (this can be found out on each beatmap website)
- [ ] If everything is set to go start "preprocess.py" and wait for it to finish for both data and input (this creates 2 .csvs "output" for the data folder and "input" for the input folder)
- [ ] Once the preprocesing has finished you can run main.py and see the results for the RandomForestRegressor model!
- [ ] Optionally you can edit preprocess or main to only preprocess 1 of the 2 folders or main to use only specific features!

## List of all features used (depening on settings in main)
- 'bpm', BPM of the song
- 'diffcount', amounts of osu! difficultys
- 'ranked_date', seconds since epoch ranked date
- 'difficultyrating', rating of each difficulty (shared value for mapsets)
- 'favourite_p', percentage value in float for favourites
- 'favourite_count', total amount of favourites
- 'language', language of the song
- 'genre', genre of the song
- 'creator', creator id of the map
- 'playcount', how many people played the map
- 'passcount', how many people passed the map
- 'successrate', how many percent passed the map
- 'total_lengths', total song length
- 'ar_in_order', approach rate of the map
- 'cs_in_order', circle size of the map
- 'hp_in_order', health loss of the map
- 'od_in_order', overall difficulty of the map
- 'aim_difficulty', aim difficulty value from osu! officially
- 'approach_rate_diff', approach rate diff value from osu! officially
- 'overall_difficulty', overall difficulty value from osu! officially 
- 'slider_factor', slider factor value from osu! officially
- 'speed_difficulty', speed difficulty value from osu! officially
- 'speed_note_count', speed note count value from osu! officially
- 'top_map_player', top map player ID
- 'pp_value', best pp value out of the top 50 map players (performance points)
- 'max_v', max velocity in map
- 'mean_v', mean velocity in map
- 'max_x', max distance in map
- 'min_t', minimal time window
- 'mean_x', mean distance in map
- 'max_a', max acceleration in map
- 'mean_a', mean acceleration in map
- 'max_rhythm_complexity', hardest pattern in map (hit circle amount / timewindow)
- 'max_angle', max angle in the map
- 'min_angle', min angle in the map
- 'mean_angle', mean angle in the map
- '40-80 Hz', Average Amount of frequencys in this field
- '80-250 Hz', Average Amount of frequencys in this field
- '250-600 Hz', Average Amount of frequencys in this field
- '600-4000 Hz', Average Amount of frequencys in this field
- '4000-6000 Hz', Average Amount of frequencys in this field
- '6000-8000 Hz', Average Amount of frequencys in this field
- '8000-20000 Hz', Average Amount of frequencys in this field 
- 'Avg of IV 1', Average of total amplitudes per time in Interval
- 'Avg of IV 2', Average of total amplitudes per time in Interval
- 'Avg of IV 3', Average of total amplitudes per time in Interval
- 'Avg of IV 4', Average of total amplitudes per time in Interval
- 'Avg of IV 5', Average of total amplitudes per time in Interval
- 'Avg of IV 6', Average of total amplitudes per time in Interval
- 'Avg of IV 7', Average of total amplitudes per time in Interval
- 'Avg of IV 8', Average of total amplitudes per time in Interval
- 'Avg of IV 9', Average of total amplitudes per time in Interval
- 'Avg of IV 10', Average of total amplitudes per time in Interval
- '3 Percent of IV 1', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 2', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 3', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 4', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 5', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 6', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 7', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 8', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 9', 3 Percent lowest value of total amplitudes per time in Interval
- '3 Percent of IV 10', 3 Percent lowest value of total amplitudes per time in Interval
- '97 Percent of IV 1', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 2', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 3', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 4', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 5', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 6', 97 Percent highest value of total amplitudess per time in Interval
- '97 Percent of IV 7', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 8', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 9', 97 Percent highest value of total amplitudes per time in Interval
- '97 Percent of IV 10', 97 Percent highest value of total amplitudes per time in Interval

## Current Problems with no solution:

- Difficultys of a mapset share the rating from the mapset
- Intervals are varying depending on total map length
- Not a real life application (more features than possible in a real case scenario)
- Problems with predicting low values (probably not fixable, only if perfect feature can be spotted)
- For better Performance a Comment Analysis should be done to filter for keywords like: good, awesome or bad, terrible

## License

GNU GPLv3