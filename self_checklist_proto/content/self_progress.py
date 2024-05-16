from .checklist import *
from .screen import *

colour_gradient = [
  "rgb(167, 175, 198)",
  "rgb(247, 227, 225)",
  "rgb(215, 215, 234)",
  "rgb(193, 186, 221)",
  "rgb(119, 137, 174)",
  "rgb(241, 237, 247)",
  "rgb(241, 216, 231)",
  "rgb(189, 181, 218)",
  "rgb(156, 215, 242)",
]

introduction_screens = ScreenSet("checklist/self-progress", [
  Screen([
    ScreenItemImage("imgs/workspace.png"),
    ScreenItemText("introduction/life-as-student-1"),
    ScreenItemText("introduction/life-as-student-2")
  ]),
  Screen([
    ScreenItemCard("introduction/mental-health", "imgs/woman_and_cat.png", 2),
    ScreenItemCard("introduction/studying", "imgs/reading_tablet.png", 9),
    ScreenItemCard("introduction/living", "imgs/teamwork_puzzle.png", 9),
    ScreenItemText("introduction/total-questions")
  ]),
  Screen([
    ScreenItemImage("imgs/woman_in_laptop.png"),
    ScreenItemText("introduction/recommend-links")
  ]),
  Screen([
    ScreenItemImage("imgs/graphs_and_stats.png"),
    ScreenItemText("introduction/see-results")
  ]),
  Screen([
    ScreenItemImage("imgs/man_using_laptop.png"),
    ScreenItemText("introduction/english-translations")
  ])
])

self_progress = Checklist(
  "self-progress/title",
  Progression([
    ProgressionStep("introduction", "imgs/DAY0.png", "imgs/DAY0 FINISH.png", None, finished=True),
    ProgressionStep("mental-health", "imgs/DAY1.png", "imgs/DAY1 FINISH.png", "psych-adaptation"),
    ProgressionStep("study-life", "imgs/DAY2.png", "imgs/DAY2 FINISH.png", "arriving-uk"),
    ProgressionStep("social-life", "imgs/DAY3.png", "imgs/DAY3 FINISH.png", "living-adaptation"),
    ProgressionStep("results", "imgs/DAY4.png", "imgs/DAY4 FINISH.png", "result"),
  ]),
  [
    Section(
      "psych-adaptation",
      "self-progress/psych-adaptation/title",
      [
        Item(
          "self-progress/psych-adaptation/arrive-feeling",
          ContentSurvey(
            "arrive-feeling",
            [
              ContentSurveyOption("excited", "self-progress/psych-adaptation/arrive-feeling/excited", colour_gradient[0]),
              ContentSurveyOption("happy", "self-progress/psych-adaptation/arrive-feeling/happy", colour_gradient[1]),
              ContentSurveyOption("anxious", "self-progress/psych-adaptation/arrive-feeling/anxious", colour_gradient[2]),
              ContentSurveyOption("homesick", "self-progress/psych-adaptation/arrive-feeling/homesick", colour_gradient[3]),
              ContentSurveyOption("disapointed", "self-progress/psych-adaptation/arrive-feeling/disapointed", colour_gradient[4]),
              ContentSurveyOption("depressed", "self-progress/psych-adaptation/arrive-feeling/depressed", colour_gradient[5]),
              ContentSurveyOption("confused", "self-progress/psych-adaptation/arrive-feeling/confused", colour_gradient[6]),
              ContentSurveyOption("lonely", "self-progress/psych-adaptation/arrive-feeling/lonely", colour_gradient[7]),
              ContentSurveyOption("other", "self-progress/psych-adaptation/arrive-feeling/other", colour_gradient[8], free_text=True),
            ],
            [
              ContentSurveyFollowup(
                ["excited", "happy"], 
                "self-progress/psych-adaptation/arrive-feeling/followup/positive"
              ),
              ContentSurveyFollowup(
                ["anxious", "homesick", "disapointed", "depressed", "confused", "lonely", "other"],
                "self-progress/psych-adaptation/arrive-feeling/followup/negative"
              )
            ]
          )
        ),
        Item(
          "self-progress/psych-adaptation/area-impact",
          ContentSurvey(
            "area-impact",
            [
              ContentSurveyOption("pressure", "self-progress/psych-adaptation/area-impact/pressure", colour_gradient[0]),
              ContentSurveyOption("study", "self-progress/psych-adaptation/area-impact/study", colour_gradient[1]),
              ContentSurveyOption("language", "self-progress/psych-adaptation/area-impact/language", colour_gradient[2]),
              ContentSurveyOption("friend", "self-progress/psych-adaptation/area-impact/friend", colour_gradient[3]),
              ContentSurveyOption("missing", "self-progress/psych-adaptation/area-impact/missing", colour_gradient[4]),
              ContentSurveyOption("different", "self-progress/psych-adaptation/area-impact/different", colour_gradient[5]),
              ContentSurveyOption("unfamiliar", "self-progress/psych-adaptation/area-impact/unfamiliar", colour_gradient[6]),
              ContentSurveyOption("other", "self-progress/psych-adaptation/area-impact/other", colour_gradient[7]),
            ]
          )
        )
      ]
    ),
    Section(
      "arriving-uk",
      "self-progress/arriving-uk/title",
      [
        Item(
          "self-progress/arriving-uk/get-brp",
          ContentList("get-brp", None)
        ),
        Item(
          "self-progress/arriving-uk/gp-reg",
          ContentList(
            "gp-reg",
            [
              ContentListEntry("self-progress/arriving-uk/gp-reg/1"),
              ContentListEntry("self-progress/arriving-uk/gp-reg/2"),
              ContentListEntry("self-progress/arriving-uk/gp-reg/3"),
              ContentListEntry("self-progress/arriving-uk/gp-reg/4"),
              ContentListEntry("self-progress/arriving-uk/gp-reg/5"),
              ContentListEntry("self-progress/arriving-uk/gp-reg/6"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/bank-card",
          ContentList(
            "bank-card",
            [
              ContentListEntry("self-progress/arriving-uk/bank-card/1"),
              ContentListEntry("self-progress/arriving-uk/bank-card/2"),
              ContentListEntry("self-progress/arriving-uk/bank-card/3"),
              ContentListEntry("self-progress/arriving-uk/bank-card/4"),
              ContentListEntry("self-progress/arriving-uk/bank-card/5"),
              ContentListEntry("self-progress/arriving-uk/bank-card/6"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/sim-card",
          ContentList(
            "sim-card",
            [
              ContentListEntry("self-progress/arriving-uk/sim-card/1"),
              ContentListEntry("self-progress/arriving-uk/sim-card/2"),
              ContentListEntry("self-progress/arriving-uk/sim-card/3"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/get-accommodation",
          ContentList(
            "get-accommodation",
            [
              ContentListEntry("self-progress/arriving-uk/get-accommodation/1"),
              ContentListEntry("self-progress/arriving-uk/get-accommodation/2")
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/oyster-card",
          ContentList(
            "oyster-card",
            [
              ContentListEntry("self-progress/arriving-uk/oyster-card/1"),
              ContentListEntry("self-progress/arriving-uk/oyster-card/2"),
              ContentListEntry("self-progress/arriving-uk/oyster-card/3"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/daily-needs",
          ContentList("daily-needs", None)
        ),
        Item(
          "self-progress/arriving-uk/find-people",
          ContentList("find-people", None)
        ),
        Item(
          "self-progress/arriving-uk/explore-city",
          ContentList("explore-city", None)
        ),
      ]
    ),
    Section(
      "living-adaptation",
      "self-progress/introduction/title",
      [
        Item(
          None,
          ContentBody("self-progress/introduction")
        )
      ]
    ),
  ]
)


