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
  "rgb(215, 181, 242)",
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
  Progression(
    "imgs/journey.png",
    [
      ProgressionStep("introduction", "imgs/DAY0.png", "imgs/DAY0 FINISH.png", None, finished=True),
      ProgressionStep("mental-health", "imgs/DAY1.png", "imgs/DAY1 FINISH.png", "psych-adaptation"),
      ProgressionStep("study-life", "imgs/DAY2.png", "imgs/DAY2 FINISH.png", "arriving-uk"),
      ProgressionStep("social-life", "imgs/DAY3.png", "imgs/DAY3 FINISH.png", "study-life"),
      ProgressionStep("results", "imgs/DAY4.png", "imgs/DAY4 FINISH.png", "results"),
    ]
  ),
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
          "self-progress/arriving-uk/unpacking",
          ContentList("unpacking", None)
        ),
        Item(
          "self-progress/arriving-uk/welcome-week",
          ContentList(
            "welcome-week",
            [
              ContentListEntry("self-progress/arriving-uk/welcome-week/1"),
              ContentListEntry("self-progress/arriving-uk/welcome-week/2"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/daily-goods",
          ContentList(
            "daily-goods",
            [
              ContentListEntry("self-progress/arriving-uk/daily-goods/1"),
              ContentListEntry("self-progress/arriving-uk/daily-goods/2"),
              ContentListEntry("self-progress/arriving-uk/daily-goods/3"),
              ContentListEntry("self-progress/arriving-uk/daily-goods/4"),
              ContentListEntry("self-progress/arriving-uk/daily-goods/5"),
              ContentListEntry("self-progress/arriving-uk/daily-goods/6"),
            ]
          )
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
              ContentListEntry("self-progress/arriving-uk/get-accommodation/2"),
              ContentListEntry("self-progress/arriving-uk/get-accommodation/3"),
              ContentListEntry("self-progress/arriving-uk/get-accommodation/4"),
              ContentListEntry("self-progress/arriving-uk/get-accommodation/5"),
              ContentListEntry("self-progress/arriving-uk/get-accommodation/6"),
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
              ContentListEntry("self-progress/arriving-uk/oyster-card/4"),
              ContentListEntry("self-progress/arriving-uk/oyster-card/5"),
              ContentListEntry("self-progress/arriving-uk/oyster-card/6"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/find-people",
          ContentList(
            "find-people",
            [
              ContentListEntry("self-progress/arriving-uk/find-people/1"),
              ContentListEntry("self-progress/arriving-uk/find-people/2"),
              ContentListEntry("self-progress/arriving-uk/find-people/3"),
              ContentListEntry("self-progress/arriving-uk/find-people/4"),
              ContentListEntry("self-progress/arriving-uk/find-people/5"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/explore-city",
          ContentList(
            "explore-city",
            [
              ContentListEntry("self-progress/arriving-uk/explore-city/1"),
              ContentListEntry("self-progress/arriving-uk/explore-city/2"),
            ]
          )
        ),
        Item(
          "self-progress/arriving-uk/local-culture",
          ContentList(
            "local-culture",
            [
              ContentListEntry("self-progress/arriving-uk/local-culture/1"),
              ContentListEntry("self-progress/arriving-uk/local-culture/2"),
            ]
          )
        ),
      ]
    ),
    Section(
      "study-life",
      "self-progress/study-life/title",
      [
        Item(
          "self-progress/study-life/explore-uni",
          ContentList(
            "explore-uni",
            [
              ContentListEntry("self-progress/study-life/explore-uni/1"),
              ContentListEntry("self-progress/study-life/explore-uni/2"),
            ]
          )
        ),
        Item(
          "self-progress/study-life/study-prep",
          ContentList(
            "study-prep",
            [
              ContentListEntry("self-progress/study-life/study-prep/1"),
              ContentListEntry("self-progress/study-life/study-prep/2"),
            ]
          )
        ),
        Item(
          "self-progress/study-life/teaching-system",
          ContentList(
            "teaching-system",
            [
              ContentListEntry("self-progress/study-life/teaching-system/1"),
              ContentListEntry("self-progress/study-life/teaching-system/2"),
              ContentListEntry("self-progress/study-life/teaching-system/3"),
              ContentListEntry("self-progress/study-life/teaching-system/4"),
              ContentListEntry("self-progress/study-life/teaching-system/5"),
            ]
          )
        ),
        Item(
          "self-progress/study-life/solo-study",
          ContentSurvey(
            "solo-study",
            [
              ContentSurveyOption("prepare_materials", "self-progress/study-life/solo-study/1/option/1", colour_gradient[0]),
              ContentSurveyOption("read_lit", "self-progress/study-life/solo-study/1/option/2", colour_gradient[1]),
              ContentSurveyOption("study_time", "self-progress/study-life/solo-study/1/option/3", colour_gradient[2]),
              ContentSurveyOption("study_method", "self-progress/study-life/solo-study/1/option/4", colour_gradient[3]),
              ContentSurveyOption("self_learn", "self-progress/study-life/solo-study/1/option/5", colour_gradient[4]),
              ContentSurveyOption("catch_up", "self-progress/study-life/solo-study/1/option/6", colour_gradient[5]),
              ContentSurveyOption("check_schedule", "self-progress/study-life/solo-study/1/option/7", colour_gradient[6]),
              ContentSurveyOption("find_criteria", "self-progress/study-life/solo-study/1/option/8", colour_gradient[7]),
              ContentSurveyOption("choose_course", "self-progress/study-life/solo-study/1/option/9", colour_gradient[8]),
              ContentSurveyOption("take_initiative", "self-progress/study-life/solo-study/1/option/10", colour_gradient[9]),
            ],
            [
              ContentSurveyFollowup([], "self-progress/study-life/solo-study-result")
            ],
            subtitle="self-progress/study-life/solo-study/1",
            hide_graph=True
          )
        ),
        Item(
          "self-progress/study-life/academic-standards",
          ContentList(
            "academic-standards",
            [
              ContentListEntry("self-progress/study-life/academic-standards/1"),
              ContentListEntry("self-progress/study-life/academic-standards/2"),
              ContentListEntry("self-progress/study-life/academic-standards/3"),
            ]
          )
        ),
        Item(
          "self-progress/study-life/language-learning/1",
          ContentSurvey(
            "language-learning",
            [
              ContentSurveyOption("often", "self-progress/study-life/language-learning/1/option/1", colour_gradient[0]),
              ContentSurveyOption("occasionally", "self-progress/study-life/language-learning/1/option/2", colour_gradient[1]),
              ContentSurveyOption("hardly", "self-progress/study-life/language-learning/1/option/3", colour_gradient[2]),
              ContentSurveyOption("not_at_all", "self-progress/study-life/language-learning/1/option/4", colour_gradient[3]),
            ],
            [
              ContentSurveyFollowup(["often", "occasionally", "hardly"], "self-progress/study-life/language-learning/2")
            ]
          )
        ),
        Item(
          "self-progress/study-life/language-learning",
          ContentList(
            "language-learning",
            [
              ContentListEntry("self-progress/study-life/language-learning/3"),
              ContentListEntry("self-progress/study-life/language-learning/4"),
              ContentListEntry("self-progress/study-life/language-learning/5"),
              ContentListEntry("self-progress/study-life/language-learning/6"),
              ContentListEntry("self-progress/study-life/language-learning/7"),
              ContentListEntry("self-progress/study-life/language-learning/8"),
              ContentListEntry("self-progress/study-life/language-learning/9"),
              ContentListEntry("self-progress/study-life/language-learning/10"),
              ContentListEntry("self-progress/study-life/language-learning/11"),
              ContentListEntry("self-progress/study-life/language-learning/12"),
            ]
          )
        ),
        Item(
          "self-progress/study-life/uni-tutors",
          ContentList(
            "uni-tutors",
            [
              ContentListEntry("self-progress/study-life/uni-tutors/1"),
              ContentListEntry("self-progress/study-life/uni-tutors/2"),
              ContentListEntry("self-progress/study-life/uni-tutors/3"),
              ContentListEntry("self-progress/study-life/uni-tutors/4"),
            ]
          )
        ),
      ]
    ),
    ResultsSection(
      "results",
      "self-progress/results/personal-title",
      "self-progress/results/global-title",
      "self-progress/results/common-pattern",
      "self-progress/results/top-five-complete",
      "self-progress/results/top-five-forgot",
      [
        SurveySummary(
          "arrive-feeling",
          "self-progress/results/arrive-feeling",
          [0, 2, 4],
          [
            "self-progress/results/arrive-feeling/1",
            "self-progress/results/arrive-feeling/2",
            "self-progress/results/arrive-feeling/3",
            "self-progress/results/arrive-feeling/4",
          ],
          ["excited", "happy"],
          exclude_from_common=True
        ),
        SurveySummary(
          "arriving-uk",
          "self-progress/results/arriving-uk",
          [3, 6, 9],
          [
            "self-progress/results/arriving-uk/1",
            "self-progress/results/arriving-uk/2",
            "self-progress/results/arriving-uk/3",
            "self-progress/results/arriving-uk/4",
          ]
        ),
        SurveySummary(
          "study-life",
          "self-progress/results/study-life",
          [2, 4, 6],
          [
            "self-progress/results/study-life/1",
            "self-progress/results/study-life/2",
            "self-progress/results/study-life/3",
            "self-progress/results/study-life/4",
          ]
        )
      ]
    )
  ]
)


