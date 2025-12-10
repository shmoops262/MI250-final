"""Travel story content and helpers for the choose-your-own-adventure program."""
from dataclasses import dataclass
from typing import Dict, List, Optional, Tuple


@dataclass(frozen=True)
class JourneyOption:
    prompt: str
    next_id: str
    location: Optional[Tuple[str, float, float]] = None
    detail: str = ""


@dataclass(frozen=True)
class StoryNode:
    node_id: str
    title: str
    description: str
    options: List[JourneyOption]


def _build_story_graph() -> Dict[str, StoryNode]:
    """Create the narrative graph describing every choice."""

    return {
        "start": StoryNode(
            node_id="start",
            title="Graduation Day in East Lansing",
            description=(
                "The Breslin Center empties as you hold your Michigan State diploma. "
                "Friends cheer, the Red Cedar glimmers, and the world suddenly feels wide open."
            ),
            options=[
                JourneyOption(
                    prompt="Take a hospitality job at Circa Resort in Las Vegas",
                    next_id="circa_start",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Neon lights and hospitality hustle await.",
                ),
                JourneyOption(
                    prompt="Return home to Grand Rapids to regroup",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Home cooking and family laughs sound great.",
                ),
                JourneyOption(
                    prompt="Jump on a plane to backpack Europe with friends",
                    next_id="europe_intro",
                    location=("London, United Kingdom", 51.50722, -0.1275),
                    detail="A rail pass and endless espresso shots in your future.",
                ),
                JourneyOption(
                    prompt="Slow road trip around the Great Lakes before deciding",
                    next_id="lakes_loop",
                    location=("Mackinac Island, Michigan", 45.8481, -84.6189),
                    detail="Freshwater horizons calm the decision-making nerves.",
                ),
            ],
        ),
        "circa_start": StoryNode(
            node_id="circa_start",
            title="Circa Resort Orientation",
            description=(
                "Your Circa badge shines as you learn the ins and outs of the casino floor."
            ),
            options=[
                JourneyOption(
                    prompt="Follow coworkers on a weekend trip to Zion National Park",
                    next_id="zion",
                    location=("Zion National Park, Utah", 37.2982, -113.0263),
                    detail="Swap neon for sandstone cathedrals.",
                ),
                JourneyOption(
                    prompt="Stay in Vegas to network at a rooftop pool party",
                    next_id="vegas_local",
                    location=("Las Vegas Strip", 36.1147, -115.1728),
                    detail="Build connections under desert stars.",
                ),
                JourneyOption(
                    prompt="Fly back to East Lansing for a quick reunion",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Share early career stories with campus friends.",
                ),
            ],
        ),
        "zion": StoryNode(
            node_id="zion",
            title="Zion Canyon",
            description=(
                "You conquer Angel's Landing and watch the canyon glow. The hike makes you wonder how many horizons you can chase."
            ),
            options=[
                JourneyOption(
                    prompt="Fly to Barcelona to keep the adventure rolling",
                    next_id="barcelona",
                    location=("Barcelona, Spain", 41.3874, 2.1686),
                    detail="Tapas and Gaudí architecture feel like a dream.",
                ),
                JourneyOption(
                    prompt="Return to Vegas with a calmer mindset",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="You jot canyon-inspired ideas for lobby designs.",
                ),
                JourneyOption(
                    prompt="Visit San Francisco for a hospitality tech meetup",
                    next_id="san_francisco",
                    location=("San Francisco, California", 37.7749, -122.4194),
                    detail="Foggy mornings pair with big career ideas.",
                ),
            ],
        ),
        "vegas_local": StoryNode(
            node_id="vegas_local",
            title="Las Vegas Local",
            description=(
                "You memorize shortcuts through the Strip and know the best late-night tacos. "
                "Coworkers trust you to lead a new themed weekend."
            ),
            options=[
                JourneyOption(
                    prompt="Propose a Spartans-themed lobby takeover back on campus",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Green and white pride returns to your plans.",
                ),
                JourneyOption(
                    prompt="Take a desert detour to the Grand Canyon",
                    next_id="grand_canyon",
                    location=("Grand Canyon, Arizona", 36.1069, -112.1129),
                    detail="Sunrise over painted cliffs never disappoints.",
                ),
                JourneyOption(
                    prompt="Accept an exchange program in Seoul",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Street food and skyscrapers remix your hospitality ideas.",
                ),
            ],
        ),
        "grand_canyon": StoryNode(
            node_id="grand_canyon",
            title="Grand Canyon Sunrise",
            description="Colors shift from violet to gold as you plot your next move over a thermos of coffee.",
            options=[
                JourneyOption(
                    prompt="Fly to Anchorage for a cooler adventure",
                    next_id="anchorage",
                    location=("Anchorage, Alaska", 61.2181, -149.9003),
                    detail="Trade desert heat for glacier breezes.",
                ),
                JourneyOption(
                    prompt="Return to Vegas and pitch a stargazing event",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="You now have sunrise photos to inspire guests.",
                ),
                JourneyOption(
                    prompt="Catch a flight to Dublin to meet traveling friends",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Music, tea, and storytelling await overseas.",
                ),
            ],
        ),
        "san_francisco": StoryNode(
            node_id="san_francisco",
            title="Golden Gate Brainstorm",
            description=(
                "Fog spills over the bridge as you meet designers merging hospitality with tech. "
                "They invite you to Tokyo for a research sprint."
            ),
            options=[
                JourneyOption(
                    prompt="Join them in Tokyo to study capsule hotels",
                    next_id="tokyo",
                    location=("Tokyo, Japan", 35.6762, 139.6503),
                    detail="Minimalist design sparks big ideas.",
                ),
                JourneyOption(
                    prompt="Return to Vegas with new app prototypes",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Circa leadership loves your innovation streak.",
                ),
                JourneyOption(
                    prompt="Fly back to East Lansing to share insights with students",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Mentoring future grads feels rewarding.",
                ),
            ],
        ),
        "east_lansing_visit": StoryNode(
            node_id="east_lansing_visit",
            title="Return to Campus",
            description=(
                "You stroll past Beaumont Tower. Students ask how you balanced risk and stability after graduation."
            ),
            options=[
                JourneyOption(
                    prompt="Host a workshop then drive to Chicago for a weekend",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="Big city energy pairs with deep-dish debates.",
                ),
                JourneyOption(
                    prompt="Fly to Dublin to reconnect with backpacking friends",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Folk music and poetry nights call you back.",
                ),
                JourneyOption(
                    prompt="Stay a while in Michigan and visit Grand Rapids",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Family dinners reset your pace.",
                ),
            ],
        ),
        "grand_rapids": StoryNode(
            node_id="grand_rapids",
            title="Grand Rapids Reset",
            description=(
                "Your childhood room now holds souvenirs. Downtown breweries buzz, and you feel both grounded and restless."
            ),
            options=[
                JourneyOption(
                    prompt="Road trip up to Traverse City for cherry pie and dunes",
                    next_id="traverse_city",
                    location=("Traverse City, Michigan", 44.7631, -85.6206),
                    detail="Lake Michigan horizons help you think clearly.",
                ),
                JourneyOption(
                    prompt="Cross the border to Toronto for a quick city swap",
                    next_id="toronto",
                    location=("Toronto, Canada", 43.6532, -79.3832),
                    detail="Skyline views pair with streetcar rides.",
                ),
                JourneyOption(
                    prompt="Book a budget flight to Reykjavik for northern lights",
                    next_id="reykjavik",
                    location=("Reykjavik, Iceland", 64.1466, -21.9426),
                    detail="Trade lake-effect snow for geothermal pools.",
                ),
            ],
        ),
        "traverse_city": StoryNode(
            node_id="traverse_city",
            title="Traverse City Shoreline",
            description="Cherry pie crumbs on your hoodie, dune sands between your toes—you draft plans for what's next.",
            options=[
                JourneyOption(
                    prompt="Drive to Chicago to meet mentors",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="Train rides, skyline views, and advice sessions await.",
                ),
                JourneyOption(
                    prompt="Loop back to East Lansing for a campus panel",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Share the road trip stories with curious students.",
                ),
                JourneyOption(
                    prompt="Ferry to Milwaukee and keep the lake tour going",
                    next_id="milwaukee",
                    location=("Milwaukee, Wisconsin", 43.0389, -87.9065),
                    detail="Riverwalk cafés and lake breezes greet you.",
                ),
            ],
        ),
        "milwaukee": StoryNode(
            node_id="milwaukee",
            title="Milwaukee Riverwalk",
            description="Live music spills from the patios. You meet digital nomads who rave about Seoul's food scene.",
            options=[
                JourneyOption(
                    prompt="Fly to Seoul with your new friends",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Late-night markets and K-pop playlists energize you.",
                ),
                JourneyOption(
                    prompt="Train to Chicago for art museums and pizza",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="You sketch future hotel ideas between exhibits.",
                ),
                JourneyOption(
                    prompt="Drive back to Grand Rapids and rest",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="A quiet reset before the next leap.",
                ),
            ],
        ),
        "toronto": StoryNode(
            node_id="toronto",
            title="Toronto Skyline",
            description="Coffee in hand, you watch the CN Tower glow and chat with travelers plotting their own routes.",
            options=[
                JourneyOption(
                    prompt="Take a sleeper train to Montreal",
                    next_id="montreal",
                    location=("Montreal, Canada", 45.5019, -73.5674),
                    detail="Bagels, jazz, and bilingual street signs charm you.",
                ),
                JourneyOption(
                    prompt="Fly to New York City for Broadway lotteries",
                    next_id="new_york",
                    location=("New York City, New York", 40.7128, -74.006),
                    detail="Skyscrapers reset your sense of scale.",
                ),
                JourneyOption(
                    prompt="Head back to East Lansing to share big city stories",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Campus feels refreshed through your new lens.",
                ),
            ],
        ),
        "reykjavik": StoryNode(
            node_id="reykjavik",
            title="Reykjavik Northern Lights",
            description="Colorful roofs, hot springs, and maybe an aurora—this layover is magic.",
            options=[
                JourneyOption(
                    prompt="Continue to Matka Canyon for emerald waters",
                    next_id="matka",
                    location=("Matka Canyon, North Macedonia", 41.94, 21.317),
                    detail="Trade glaciers for limestone cliffs and kayaks.",
                ),
                JourneyOption(
                    prompt="Hop to Dublin for live music",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Folk songs and storytelling feel like home.",
                ),
                JourneyOption(
                    prompt="Fly back to Grand Rapids to regroup",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Home base welcomes tales of auroras.",
                ),
            ],
        ),
        "matka": StoryNode(
            node_id="matka",
            title="Kayaking Matka Canyon",
            description=(
                "Emerald water winds through towering cliffs. You taste burek after a long paddle and dream up future routes."
            ),
            options=[
                JourneyOption(
                    prompt="Bus to Lake Bled for more alpine serenity",
                    next_id="lake_bled",
                    location=("Lake Bled, Slovenia", 46.3683, 14.1146),
                    detail="Island chapels and mirrored peaks calm your mind.",
                ),
                JourneyOption(
                    prompt="Fly to Seoul for a work-study exchange",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Night markets and hospitality lessons await.",
                ),
                JourneyOption(
                    prompt="Return to East Lansing to share canyon stories",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Campus friends listen, wide-eyed.",
                ),
            ],
        ),
        "lake_bled": StoryNode(
            node_id="lake_bled",
            title="Lake Bled Calm",
            description="Mist rises as you row toward the island church. Reflection time feels necessary.",
            options=[
                JourneyOption(
                    prompt="Take a train to Vienna for classical concerts",
                    next_id="vienna",
                    location=("Vienna, Austria", 48.2082, 16.3738),
                    detail="Pastries and palaces spark elegant ideas.",
                ),
                JourneyOption(
                    prompt="Return to Grand Rapids with alpine inspiration",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Bring lake calm to your next plan.",
                ),
                JourneyOption(
                    prompt="Continue to Dublin for one more music-filled stop",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="The city hums with creative energy.",
                ),
            ],
        ),
        "europe_intro": StoryNode(
            node_id="europe_intro",
            title="Red-Eye to Europe",
            description="Your friends cheer as the plane lifts off. Hostels, sleeper trains, and endless espresso shots await.",
            options=[
                JourneyOption(
                    prompt="Start in Paris to celebrate graduation",
                    next_id="paris",
                    location=("Paris, France", 48.8566, 2.3522),
                    detail="Crêpes under the Eiffel Tower feel surreal.",
                ),
                JourneyOption(
                    prompt="Head straight to Matka Canyon for the kayak dream",
                    next_id="matka",
                    location=("Matka Canyon, North Macedonia", 41.94, 21.317),
                    detail="Emerald waters welcome your adventurous streak.",
                ),
                JourneyOption(
                    prompt="Kick things off in Prague for castle views",
                    next_id="prague",
                    location=("Prague, Czech Republic", 50.0755, 14.4378),
                    detail="Cobblestones echo with midnight stories.",
                ),
            ],
        ),
        "paris": StoryNode(
            node_id="paris",
            title="Paris Picnic",
            description="You picnic by the Seine, watching boats drift by as you plan the next leg.",
            options=[
                JourneyOption(
                    prompt="Train to Barcelona for coastal colors",
                    next_id="barcelona",
                    location=("Barcelona, Spain", 41.3874, 2.1686),
                    detail="Tapas crawls and beach strolls keep spirits high.",
                ),
                JourneyOption(
                    prompt="Night train to Zurich for alpine air",
                    next_id="zurich",
                    location=("Zurich, Switzerland", 47.3769, 8.5417),
                    detail="Lake views and mountain reflections calm your pace.",
                ),
                JourneyOption(
                    prompt="Budget flight to Dublin for live music",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Pub sessions and storytelling await.",
                ),
            ],
        ),
        "prague": StoryNode(
            node_id="prague",
            title="Prague Dawn",
            description=(
                "Charles Bridge glows in pastel light as artists set up easels. You sip coffee and consider your next stop."
            ),
            options=[
                JourneyOption(
                    prompt="Bus to Vienna for classical concerts",
                    next_id="vienna",
                    location=("Vienna, Austria", 48.2082, 16.3738),
                    detail="Palaces and pastries feel luxurious yet welcoming.",
                ),
                JourneyOption(
                    prompt="Fly to Athens for island hopping",
                    next_id="athens",
                    location=("Athens, Greece", 37.9838, 23.7275),
                    detail="Columns and sea breezes pair beautifully.",
                ),
                JourneyOption(
                    prompt="Head to Berlin for street art inspiration",
                    next_id="berlin",
                    location=("Berlin, Germany", 52.52, 13.405),
                    detail="Murals and techno blend into long conversations.",
                ),
            ],
        ),
        "barcelona": StoryNode(
            node_id="barcelona",
            title="Barcelona Coastline",
            description=(
                "You stroll La Barceloneta, sketching Sagrada Família spires. Tapas fuel your energy to keep exploring."
            ),
            options=[
                JourneyOption(
                    prompt="Ferry to Mallorca for beach hikes",
                    next_id="mallorca",
                    location=("Palma de Mallorca, Spain", 39.5696, 2.6502),
                    detail="Cliffside coves pair with turquoise water.",
                ),
                JourneyOption(
                    prompt="Budget flight to Marrakesh for souk adventures",
                    next_id="marrakesh",
                    location=("Marrakesh, Morocco", 31.6295, -7.9811),
                    detail="Spices, lanterns, and rooftop views reset your senses.",
                ),
                JourneyOption(
                    prompt="Join a friend heading to Seoul for a culinary festival",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Bibimbap and bingsu become your study materials.",
                ),
            ],
        ),
        "vienna": StoryNode(
            node_id="vienna",
            title="Vienna Waltz",
            description="Ornate halls echo with music. You taste Sachertorte and consider how to blend elegance into future projects.",
            options=[
                JourneyOption(
                    prompt="Return to Prague to revisit friends",
                    next_id="prague",
                    location=("Prague, Czech Republic", 50.0755, 14.4378),
                    detail="Cobblestones and café chats continue.",
                ),
                JourneyOption(
                    prompt="Fly to Berlin for street art tours",
                    next_id="berlin",
                    location=("Berlin, Germany", 52.52, 13.405),
                    detail="Murals stretch across old walls.",
                ),
                JourneyOption(
                    prompt="Return to East Lansing for a quick campus visit",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Homecoming energy fuels your next leap.",
                ),
            ],
        ),
        "berlin": StoryNode(
            node_id="berlin",
            title="Berlin Street Art",
            description="Colorful murals and open-air galleries inspire bold lobby ideas. You grab a döner kebab and map out next moves.",
            options=[
                JourneyOption(
                    prompt="Take a night train to Amsterdam",
                    next_id="amsterdam",
                    location=("Amsterdam, Netherlands", 52.3676, 4.9041),
                    detail="Bridges, bikes, and brown cafés await.",
                ),
                JourneyOption(
                    prompt="Fly to Dublin to catch a concert",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Live music and late-night tea.",
                ),
                JourneyOption(
                    prompt="Return to Vegas to pitch a mural series",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Street art inspiration fits the Strip perfectly.",
                ),
            ],
        ),
        "amsterdam": StoryNode(
            node_id="amsterdam",
            title="Amsterdam Canals",
            description="Canal boats glide as you cycle alongside. Stroopwafel crumbs sprinkle your notebook full of plans.",
            options=[
                JourneyOption(
                    prompt="Train to Paris for one more visit",
                    next_id="paris",
                    location=("Paris, France", 48.8566, 2.3522),
                    detail="Sunset picnics and gallery strolls beckon again.",
                ),
                JourneyOption(
                    prompt="Fly to Dublin to reconnect with friends",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Familiar faces and folk music feel like home.",
                ),
                JourneyOption(
                    prompt="Return to Grand Rapids for a reflective pause",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Bring Dutch bike inspiration to Michigan trails.",
                ),
            ],
        ),
        "mallorca": StoryNode(
            node_id="mallorca",
            title="Mallorca Coves",
            description="You hike down to hidden beaches with clear turquoise water. Paella aromas fill seaside towns.",
            options=[
                JourneyOption(
                    prompt="Return to Barcelona for architecture walks",
                    next_id="barcelona",
                    location=("Barcelona, Spain", 41.3874, 2.1686),
                    detail="Back to Gaudí curves and city buzz.",
                ),
                JourneyOption(
                    prompt="Fly to Berlin for art fairs",
                    next_id="berlin",
                    location=("Berlin, Germany", 52.52, 13.405),
                    detail="Gallery hopping adds new creative sparks.",
                ),
                JourneyOption(
                    prompt="Head to Dublin to reunite with friends",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Music and laughter carry into the night.",
                ),
            ],
        ),
        "marrakesh": StoryNode(
            node_id="marrakesh",
            title="Marrakesh Maze",
            description="Lantern-lit alleys and spice markets awaken every sense. Rooftops glow orange at sunset.",
            options=[
                JourneyOption(
                    prompt="Return to Barcelona with new recipes",
                    next_id="barcelona",
                    location=("Barcelona, Spain", 41.3874, 2.1686),
                    detail="Tapas meet tagine in your notebook.",
                ),
                JourneyOption(
                    prompt="Fly to Athens and island hop",
                    next_id="athens",
                    location=("Athens, Greece", 37.9838, 23.7275),
                    detail="Mediterranean breezes follow desert heat.",
                ),
                JourneyOption(
                    prompt="Travel to Seoul for a design exchange",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Patterns and textiles influence your hospitality vision.",
                ),
            ],
        ),
        "athens": StoryNode(
            node_id="athens",
            title="Athens Alleyways",
            description="Acropolis views rise above street art. Gyro vendors cheerfully offer seconds as you plan ferries to islands.",
            options=[
                JourneyOption(
                    prompt="Sail to Santorini for cliffside sunsets",
                    next_id="santorini",
                    location=("Santorini, Greece", 36.3932, 25.4615),
                    detail="Whitewashed homes and blue domes sparkle.",
                ),
                JourneyOption(
                    prompt="Return to Matka Canyon for more nature",
                    next_id="matka",
                    location=("Matka Canyon, North Macedonia", 41.94, 21.317),
                    detail="The canyon feels like a familiar sanctuary now.",
                ),
                JourneyOption(
                    prompt="Fly to Chicago to meet mentors",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="Cross-continental flight reconnects you with old guides.",
                ),
            ],
        ),
        "santorini": StoryNode(
            node_id="santorini",
            title="Santorini Sunsets",
            description="Blue domes glow against the Aegean. You journal about gratitude while boats drift below.",
            options=[
                JourneyOption(
                    prompt="Return to Dublin for a city contrast",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="From island cliffs to cozy pubs overnight.",
                ),
                JourneyOption(
                    prompt="Fly to East Lansing and surprise friends",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Catch a campus sunrise with fresh perspective.",
                ),
                JourneyOption(
                    prompt="Continue to Tokyo for another long-haul adventure",
                    next_id="tokyo",
                    location=("Tokyo, Japan", 35.6762, 139.6503),
                    detail="Trade blue domes for neon crossings.",
                ),
            ],
        ),
        "tokyo": StoryNode(
            node_id="tokyo",
            title="Tokyo Lights",
            description=(
                "Shibuya Crossing swirls with organized chaos. You sample ramen, test onsen etiquette, and collect design notes."
            ),
            options=[
                JourneyOption(
                    prompt="Take the bullet train to Kyoto for temples",
                    next_id="kyoto",
                    location=("Kyoto, Japan", 35.0116, 135.7681),
                    detail="Torii gates and tea ceremonies slow your pace.",
                ),
                JourneyOption(
                    prompt="Return to Seoul to collaborate on a project",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="A familiar skyline with new ideas brewing.",
                ),
                JourneyOption(
                    prompt="Fly back to Vegas to implement minimalist designs",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Sleek concepts meet neon palettes.",
                ),
            ],
        ),
        "kyoto": StoryNode(
            node_id="kyoto",
            title="Kyoto Temples",
            description="You walk beneath rows of red torii gates, the scent of cedar in the air. A tea ceremony teaches patience.",
            options=[
                JourneyOption(
                    prompt="Return to Tokyo for one more night",
                    next_id="tokyo",
                    location=("Tokyo, Japan", 35.6762, 139.6503),
                    detail="Neon energy after temple calm feels electric.",
                ),
                JourneyOption(
                    prompt="Fly to Anchorage to chase northern lights",
                    next_id="anchorage",
                    location=("Anchorage, Alaska", 61.2181, -149.9003),
                    detail="Trade lanterns for auroras as you cross the Pacific.",
                ),
                JourneyOption(
                    prompt="Head to Dublin for a long layover of music",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="East meets west in your travel journal.",
                ),
            ],
        ),
        "seoul": StoryNode(
            node_id="seoul",
            title="Seoul Hospitality Exchange",
            description=(
                "You shadow managers at a high-rise hotel by day and snack through Myeongdong by night. "
                "A dance crew invites you to rehearsal."
            ),
            options=[
                JourneyOption(
                    prompt="Fly to Tokyo for a design sprint",
                    next_id="tokyo",
                    location=("Tokyo, Japan", 35.6762, 139.6503),
                    detail="Minimalist aesthetics spark new lobby ideas.",
                ),
                JourneyOption(
                    prompt="Return to Vegas with international inspiration",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="You arrive with notebooks full of sketches.",
                ),
                JourneyOption(
                    prompt="Fly home through Anchorage for northern views",
                    next_id="anchorage",
                    location=("Anchorage, Alaska", 61.2181, -149.9003),
                    detail="Glaciers from the plane window feel humbling.",
                ),
            ],
        ),
        "anchorage": StoryNode(
            node_id="anchorage",
            title="Anchorage Layover",
            description="You peer at glaciers from the plane, then sip coffee while mountains watch over the city.",
            options=[
                JourneyOption(
                    prompt="Head south to Seattle for a coastal ride",
                    next_id="seattle",
                    location=("Seattle, Washington", 47.6062, -122.3321),
                    detail="Pike Place, ferries, and fresh salmon highlight the stop.",
                ),
                JourneyOption(
                    prompt="Fly back to East Lansing with a northern story",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Campus welcomes tales of tundra winds.",
                ),
                JourneyOption(
                    prompt="Continue to Tokyo and chase sunrise across the Pacific",
                    next_id="tokyo",
                    location=("Tokyo, Japan", 35.6762, 139.6503),
                    detail="Jet lag pairs with pure excitement.",
                ),
            ],
        ),
        "seattle": StoryNode(
            node_id="seattle",
            title="Seattle Stopover",
            description=(
                "Rain taps the market awnings as you watch ferries move across the Sound. "
                "You sample salmon chowder and debate future routes."
            ),
            options=[
                JourneyOption(
                    prompt="Take a coastal train to San Francisco",
                    next_id="san_francisco",
                    location=("San Francisco, California", 37.7749, -122.4194),
                    detail="A scenic ride links coffee culture cities.",
                ),
                JourneyOption(
                    prompt="Fly to Seoul to continue your exchange",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Airport lounges blur as adventures stack.",
                ),
                JourneyOption(
                    prompt="Return to Anchorage to plan a glacier hike",
                    next_id="anchorage",
                    location=("Anchorage, Alaska", 61.2181, -149.9003),
                    detail="Icy peaks keep calling you back north.",
                ),
            ],
        ),
        "zurich": StoryNode(
            node_id="zurich",
            title="Zurich Layover",
            description="You sit beside the Limmat River, jotting notes for a travel blog. Snow-capped peaks remind you to slow down.",
            options=[
                JourneyOption(
                    prompt="Ride a panoramic train to Milan",
                    next_id="milan",
                    location=("Milan, Italy", 45.4642, 9.19),
                    detail="Fashion windows and espresso shots keep you alert.",
                ),
                JourneyOption(
                    prompt="Head to Berlin for street art inspiration",
                    next_id="berlin",
                    location=("Berlin, Germany", 52.52, 13.405),
                    detail="Murals and techno blend into long conversations.",
                ),
                JourneyOption(
                    prompt="Rejoin friends in Paris for one more picnic",
                    next_id="paris",
                    location=("Paris, France", 48.8566, 2.3522),
                    detail="Sunset along the Seine never gets old.",
                ),
            ],
        ),
        "milan": StoryNode(
            node_id="milan",
            title="Milan Momentum",
            description="Runways and ornate galleries surround you. You spot boutique hotels that blend art and comfort.",
            options=[
                JourneyOption(
                    prompt="Train to Zurich for alpine calm",
                    next_id="zurich",
                    location=("Zurich, Switzerland", 47.3769, 8.5417),
                    detail="Lake reflections encourage a slower pace.",
                ),
                JourneyOption(
                    prompt="Fly to Barcelona for seaside tapas",
                    next_id="barcelona",
                    location=("Barcelona, Spain", 41.3874, 2.1686),
                    detail="A familiar coastline welcomes you back.",
                ),
                JourneyOption(
                    prompt="Return to Vegas to bring fashion-forward ideas",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Elevated aesthetics meet neon flair.",
                ),
            ],
        ),
        "dublin": StoryNode(
            node_id="dublin",
            title="Dublin Storytelling",
            description=(
                "Live music spills from doorways, and friends gather to trade travel tales. "
                "Someone hands you a notebook and asks for your favorite moments."
            ),
            options=[
                JourneyOption(
                    prompt="Take a ferry to London and continue exploring",
                    next_id="london",
                    location=("London, United Kingdom", 51.50722, -0.1275),
                    detail="Markets, museums, and double-deckers await.",
                ),
                JourneyOption(
                    prompt="Fly back to East Lansing with a suitcase of souvenirs",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Time to show everyone your passport stamps.",
                ),
                JourneyOption(
                    prompt="Head to Reykjavik for another chance at auroras",
                    next_id="reykjavik",
                    location=("Reykjavik, Iceland", 64.1466, -21.9426),
                    detail="Maybe this is the night the sky dances.",
                ),
            ],
        ),
        "london": StoryNode(
            node_id="london",
            title="London Layover",
            description=(
                "Rain taps the Thames while you watch street performers on the South Bank. "
                "You sip tea and circle more destinations on your map."
            ),
            options=[
                JourneyOption(
                    prompt="Train up to Edinburgh for dramatic cliffs",
                    next_id="edinburgh",
                    location=("Edinburgh, Scotland", 55.9533, -3.1883),
                    detail="Bagpipes echo as you climb Arthur's Seat.",
                ),
                JourneyOption(
                    prompt="Fly to Chicago to reconnect with mentors",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="Jet lag meets deep-dish pizza debates.",
                ),
                JourneyOption(
                    prompt="Return to Grand Rapids for a surprise visit",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Family cheers as you ring the doorbell.",
                ),
            ],
        ),
        "edinburgh": StoryNode(
            node_id="edinburgh",
            title="Edinburgh Overlook",
            description="The city sprawls below as you perch on Arthur's Seat. Misty air and castle views feel timeless.",
            options=[
                JourneyOption(
                    prompt="Return to Dublin for one more music night",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Your friends saved you a seat near the stage.",
                ),
                JourneyOption(
                    prompt="Fly to Reykjavik to chase northern lights",
                    next_id="reykjavik",
                    location=("Reykjavik, Iceland", 64.1466, -21.9426),
                    detail="Skyfire or bust—you're committed now.",
                ),
                JourneyOption(
                    prompt="Head back to East Lansing with stories of castles",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Campus friends love a good legend.",
                ),
            ],
        ),
        "lakes_loop": StoryNode(
            node_id="lakes_loop",
            title="Great Lakes Loop",
            description="You plan a circuit of shoreline towns, driving with the windows down and playlists full of road-trip anthems.",
            options=[
                JourneyOption(
                    prompt="Cross into Ontario to see Niagara Falls",
                    next_id="niagara",
                    location=("Niagara Falls, Canada", 43.0896, -79.0849),
                    detail="Mist on your face, rainbows in every photo.",
                ),
                JourneyOption(
                    prompt="Stay in Petoskey for sunset over Little Traverse Bay",
                    next_id="petoskey",
                    location=("Petoskey, Michigan", 45.3737, -84.9553),
                    detail="Stone beaches and quiet marinas slow time down.",
                ),
                JourneyOption(
                    prompt="Take a ferry to Door County and camp under stars",
                    next_id="door_county",
                    location=("Door County, Wisconsin", 44.8342, -87.3770),
                    detail="Lighthouses guide your overnight adventure.",
                ),
            ],
        ),
        "petoskey": StoryNode(
            node_id="petoskey",
            title="Petoskey Pause",
            description="You collect Petoskey stones and sip cherry soda. The calm town inspires journaling about what's next.",
            options=[
                JourneyOption(
                    prompt="Drive back to Grand Rapids to regroup",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Family dinners and brainstorming sessions resume.",
                ),
                JourneyOption(
                    prompt="Take the scenic route to Marquette",
                    next_id="marquette",
                    location=("Marquette, Michigan", 46.5436, -87.3956),
                    detail="Lake Superior waves crash against sandstone cliffs.",
                ),
                JourneyOption(
                    prompt="Head west toward Minneapolis for live music",
                    next_id="minneapolis",
                    location=("Minneapolis, Minnesota", 44.9778, -93.2650),
                    detail="Indie shows and art museums fill the itinerary.",
                ),
            ],
        ),
        "door_county": StoryNode(
            node_id="door_county",
            title="Door County Campfire",
            description="Cicadas hum as you roast marshmallows by Lake Michigan. You chart routes on a paper map, craving even more horizon.",
            options=[
                JourneyOption(
                    prompt="Ferry to Milwaukee and meet a cousin",
                    next_id="milwaukee",
                    location=("Milwaukee, Wisconsin", 43.0389, -87.9065),
                    detail="Custard, breweries, and lake breezes await.",
                ),
                JourneyOption(
                    prompt="Drive south to Chicago for skyline photos",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="Glass towers rise above Lake Michigan's blue.",
                ),
                JourneyOption(
                    prompt="Loop back to East Lansing for game day",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Green and white flags line Grand River Avenue.",
                ),
            ],
        ),
        "niagara": StoryNode(
            node_id="niagara",
            title="Niagara Falls Mist",
            description="Thunderous water drowns out all other sounds. A stranger tells you about hostel networks across Europe.",
            options=[
                JourneyOption(
                    prompt="Head to Toronto to chase more city energy",
                    next_id="toronto",
                    location=("Toronto, Canada", 43.6532, -79.3832),
                    detail="CN Tower selfies and streetcar rides await.",
                ),
                JourneyOption(
                    prompt="Return to Detroit for a Motown tour",
                    next_id="detroit_art",
                    location=("Detroit, Michigan", 42.3314, -83.0458),
                    detail="Music history and new murals inspire fresh playlists.",
                ),
                JourneyOption(
                    prompt="Fly to Reykjavik and keep the waterfalls theme alive",
                    next_id="reykjavik",
                    location=("Reykjavik, Iceland", 64.1466, -21.9426),
                    detail="Cold spray replaces warm mist but the thrill remains.",
                ),
            ],
        ),
        "detroit_art": StoryNode(
            node_id="detroit_art",
            title="Detroit Art Crawl",
            description="Murals, Motown, and museums fill the weekend. You realize travel has rewired how you see every city.",
            options=[
                JourneyOption(
                    prompt="Drive back to East Lansing for a quiet campus walk",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Memories flood back between brick paths.",
                ),
                JourneyOption(
                    prompt="Take the train to Toronto for another skyline",
                    next_id="toronto",
                    location=("Toronto, Canada", 43.6532, -79.3832),
                    detail="Catch up over skyline views and hockey chats.",
                ),
                JourneyOption(
                    prompt="Fly to Vegas to compare big-city vibes",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Neon signs greet you like coworkers now.",
                ),
            ],
        ),
        "marquette": StoryNode(
            node_id="marquette",
            title="Superior Cliffs in Marquette",
            description="Waves crash against Presque Isle. You roast marshmallows with hikers trading stories of far-off mountains.",
            options=[
                JourneyOption(
                    prompt="Take a ferry to Isle Royale for remote camping",
                    next_id="isle_royale",
                    location=("Isle Royale, Michigan", 48.1, -88.55),
                    detail="Moose sightings and star-sprinkled nights await.",
                ),
                JourneyOption(
                    prompt="Head back to Petoskey to regroup",
                    next_id="petoskey",
                    location=("Petoskey, Michigan", 45.3737, -84.9553),
                    detail="The quiet harbor resets your pace.",
                ),
                JourneyOption(
                    prompt="Fly to Anchorage to compare northern coasts",
                    next_id="anchorage",
                    location=("Anchorage, Alaska", 61.2181, -149.9003),
                    detail="Cold salt air and endless daylight surprise you.",
                ),
            ],
        ),
        "isle_royale": StoryNode(
            node_id="isle_royale",
            title="Isle Royale Silence",
            description="No cars, just trees, lake, and loons. The isolation sparks big ideas about sustainable travel.",
            options=[
                JourneyOption(
                    prompt="Return to Marquette with fresh perspective",
                    next_id="marquette",
                    location=("Marquette, Michigan", 46.5436, -87.3956),
                    detail="Backpacks feel lighter, decisions clearer.",
                ),
                JourneyOption(
                    prompt="Head to Minneapolis to reconnect with friends",
                    next_id="minneapolis",
                    location=("Minneapolis, Minnesota", 44.9778, -93.2650),
                    detail="Urban lakes and art museums balance out the wilderness.",
                ),
                JourneyOption(
                    prompt="Book a long-haul flight to Tokyo",
                    next_id="tokyo",
                    location=("Tokyo, Japan", 35.6762, 139.6503),
                    detail="From silence to neon in a single leap.",
                ),
            ],
        ),
        "minneapolis": StoryNode(
            node_id="minneapolis",
            title="Minneapolis Music Night",
            description="Indie bands play under string lights near the Mississippi. You compare notes with travelers mapping out similar routes.",
            options=[
                JourneyOption(
                    prompt="Ride the train to Chicago and keep moving",
                    next_id="chicago",
                    location=("Chicago, Illinois", 41.8781, -87.6298),
                    detail="Back to skyscrapers and busy sidewalks.",
                ),
                JourneyOption(
                    prompt="Drive back toward East Lansing for game day",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Tailgates and campus chants welcome you home.",
                ),
                JourneyOption(
                    prompt="Fly north to Anchorage for glacier hikes",
                    next_id="anchorage",
                    location=("Anchorage, Alaska", 61.2181, -149.9003),
                    detail="Swap guitars for crampons and keep exploring.",
                ),
            ],
        ),
        "chicago": StoryNode(
            node_id="chicago",
            title="Chicago Interlude",
            description="You admire the Bean's reflection and debate deep-dish vs. tavern-style pizza. The train map looks like an invitation.",
            options=[
                JourneyOption(
                    prompt="Hop on a flight to Los Angeles for an expo",
                    next_id="los_angeles",
                    location=("Los Angeles, California", 34.0522, -118.2437),
                    detail="Palm trees accompany the professional hustle.",
                ),
                JourneyOption(
                    prompt="Take the Wolverine train back to East Lansing",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="A cozy ride home with popcorn and playlists.",
                ),
                JourneyOption(
                    prompt="Fly to Dublin to rejoin friends overseas",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Pub music and poetry nights await.",
                ),
            ],
        ),
        "los_angeles": StoryNode(
            node_id="los_angeles",
            title="Los Angeles Expo",
            description=(
                "Workshops at the convention center teach you the future of immersive hospitality. "
                "You end the day watching the sunset from Santa Monica Pier."
            ),
            options=[
                JourneyOption(
                    prompt="Visit San Francisco to compare hospitality tech",
                    next_id="san_francisco",
                    location=("San Francisco, California", 37.7749, -122.4194),
                    detail="Foggy mornings and golden bridges mix with ideation.",
                ),
                JourneyOption(
                    prompt="Return to Vegas with a suitcase of brochures",
                    next_id="vegas_local",
                    location=("Las Vegas, Nevada", 36.17497, -115.13722),
                    detail="Implement your favorite ideas back at Circa.",
                ),
                JourneyOption(
                    prompt="Take time off and fly to Seoul for street food",
                    next_id="seoul",
                    location=("Seoul, South Korea", 37.5665, 126.978),
                    detail="Gimbap and night markets help you reset.",
                ),
            ],
        ),
        "new_york": StoryNode(
            node_id="new_york",
            title="New York Layover",
            description="You rush between Broadway lotteries and food trucks. City lights remind you of Vegas—but with skyscrapers.",
            options=[
                JourneyOption(
                    prompt="Train to Boston for a history kick",
                    next_id="boston",
                    location=("Boston, Massachusetts", 42.3601, -71.0589),
                    detail="Freedom Trail walks mix with cannoli stops.",
                ),
                JourneyOption(
                    prompt="Fly to Dublin to meet up again",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Jet lag can't stop a good fiddle session.",
                ),
                JourneyOption(
                    prompt="Return to East Lansing with big city ideas",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="You sketch skyline-inspired designs for campus cafés.",
                ),
            ],
        ),
        "boston": StoryNode(
            node_id="boston",
            title="Boston Brickwork",
            description="You stroll Beacon Hill and listen to buskers near Faneuil Hall. History feels alive.",
            options=[
                JourneyOption(
                    prompt="Return to Detroit for a Motown-infused finale",
                    next_id="detroit_art",
                    location=("Detroit, Michigan", 42.3314, -83.0458),
                    detail="Music threads together every stop you've made.",
                ),
                JourneyOption(
                    prompt="Fly to Reykjavik for a final northern lights attempt",
                    next_id="reykjavik",
                    location=("Reykjavik, Iceland", 64.1466, -21.9426),
                    detail="Maybe third time's the charm.",
                ),
                JourneyOption(
                    prompt="Head back to East Lansing and rest",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="Campus trees welcome you back.",
                ),
            ],
        ),
        "montreal": StoryNode(
            node_id="montreal",
            title="Montreal Morning",
            description="Jazz riffs mix with the aroma of fresh bagels. You feel at home in the blend of languages.",
            options=[
                JourneyOption(
                    prompt="Train to Quebec City for cobblestone charm",
                    next_id="quebec_city",
                    location=("Quebec City, Canada", 46.8139, -71.2080),
                    detail="Castle-like hotels and river views slow your pace.",
                ),
                JourneyOption(
                    prompt="Fly to Dublin to rejoin friends",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Music and poetry nights never get old.",
                ),
                JourneyOption(
                    prompt="Return to Grand Rapids with new coffee recipes",
                    next_id="grand_rapids",
                    location=("Grand Rapids, Michigan", 42.96336, -85.66809),
                    detail="Your parents love the maple latte experiment.",
                ),
            ],
        ),
        "quebec_city": StoryNode(
            node_id="quebec_city",
            title="Quebec City Quiet Streets",
            description="Cobblestones, river breezes, and a sense of history keep you strolling long after sunset.",
            options=[
                JourneyOption(
                    prompt="Return to Montreal for another jazz night",
                    next_id="montreal",
                    location=("Montreal, Canada", 45.5019, -73.5674),
                    detail="You aren't done with the sax solos yet.",
                ),
                JourneyOption(
                    prompt="Fly to East Lansing with a heart full of stories",
                    next_id="east_lansing_visit",
                    location=("East Lansing, Michigan", 42.73698, -84.48387),
                    detail="You promise to visit again soon.",
                ),
                JourneyOption(
                    prompt="Continue to Dublin to keep the adventure alive",
                    next_id="dublin",
                    location=("Dublin, Ireland", 53.3498, -6.2603),
                    detail="Friends are already saving you a spot at the session.",
                ),
            ],
        ),
    }


STORY_GRAPH = _build_story_graph()


def get_start_node_id() -> str:
    return "start"


def get_node(node_id: str) -> StoryNode:
    return STORY_GRAPH[node_id]


def describe_node(node: StoryNode) -> str:
    lines = [f"\n=== {node.title} ===", node.description, ""]
    for idx, option in enumerate(node.options, start=1):
        extra = f" — {option.detail}" if option.detail else ""
        lines.append(f"  {idx}. {option.prompt}{extra}")
    lines.append("\nType the number of your choice, or type 'quit' to finish and view your travel map.")
    return "\n".join(lines)


def record_location(option: JourneyOption) -> Optional[Tuple[str, float, float]]:
    return option.location
