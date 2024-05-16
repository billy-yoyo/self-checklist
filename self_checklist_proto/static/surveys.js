
const Survey = (() => {
  // load 
  APPS.push(() => {
    for (let i = 0; i < localStorage.length; i++) {
      const key = localStorage.key(i);
      if (key.startsWith("survey-result-") && !key.endsWith("---submitted")) {
        const surveyName = key.slice("survey-result-".length);
        try {
          const answers = JSON.parse(localStorage.getItem(key));
          loadSubmission(surveyName, answers);
        } catch {
          localStorage.removeItem(key);
        }
      }
    }
  });

  const postSubmit = async (surveyName, answers) => {
    console.log(`submitting ${surveyName} with answers ${JSON.stringify(answers)}`);
    const response = await fetch(`/survey/${surveyName}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN
      },
      body: JSON.stringify({
        answers
      })
    });

    if (200 <= response.status && response.status < 300) {
      return true;
    } else {
      console.warn(`Failed to submit, received status code: ${response.status}`)
      throw Error(`Invalid status code: ${response.status}`);
    }
  };

  const attemptSubmission = async (surveyName, answers) => {
    if (localStorage.getItem(`survey-result-${surveyName}---submitted`) === "true") {
      return;
    }
    console.log(`attempting submission for ${surveyName} with answers ${JSON.stringify(answers)}`);
    localStorage.setItem(`survey-result-${surveyName}`, JSON.stringify(answers));
    try {
      await postSubmit(surveyName, answers);
      localStorage.setItem(`survey-result-${surveyName}---submitted`, "true");
    } catch {
      localStorage.setItem(`survey-result-${surveyName}---submitted`, "false");
    }
  };

  const loadSubmission = (surveyName, answers) => {
    hideButton(surveyName);
    showChart(surveyName);
    const checkboxes = disableCheckboxes(surveyName);
    checkboxes.forEach(checkbox => {
      const option = checkbox.dataset.option;
      checkbox.checked = answers[option];
    });
    toggleFollowups(surveyName, answers);
    attemptSubmission(surveyName, answers);
  };

  const hideButton = (surveyName) => {
    const button = document.getElementById(`survey-${surveyName}-submit`);
    if (button) {
      button.classList.add("hidden");
    }
  };

  const showChart = (surveyName) => {
    const chart = document.getElementById(`survey-followup-${surveyName}`);
    if (chart) {
      chart.classList.remove("hidden");
    }
  };

  const disableCheckboxes = (surveyName) => {
    const checkboxes = Array.from(document.querySelectorAll(`input[type=checkbox][data-survey="${surveyName}"]`));
    checkboxes.forEach(checkbox => {
      checkbox.disabled = true;
    });
    return checkboxes;
  }

  const toggleFollowups = (surveyName, answers) => {
    const followups = Array.from(document.querySelectorAll(`.followup-item[data-survey="${surveyName}"]`));

    followups.forEach(followup => {
      const validAnswers = followup.dataset.answers.split(";");
      if (validAnswers.some(answer => answers[answer])) {
        followup.classList.remove("hidden");
      } else {
        followup.classList.add("hidden");
      }
    });
  };
  
  const submitSurvey = (surveyName) => {
    hideButton(surveyName);
    showChart(surveyName);
    const checkboxes = disableCheckboxes(surveyName);
    const answers = Object.fromEntries(checkboxes.map(checkbox => [checkbox.dataset.option, checkbox.checked]));

    toggleFollowups(surveyName, answers);
    attemptSubmission(surveyName, answers);
  };

  return {
    submit: submitSurvey
  }
})();
