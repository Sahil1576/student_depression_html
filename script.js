// Enum options mirrored exactly from schema.py

const CITY_OPTIONS = [
  "Kalyan", "Srinagar", "hyderabad", "vasai_virar", "lucknow", "thane",
  "ludhiana", "agra", "surat", "kolkata", "jaipur", "patna", "visakhapatnam",
  "pune", "ahmedabad", "bhopal", "chennai", "meerut", "rajkot", "delhi",
  "bangalore", "ghaziabad", "mumbai", "vadodara", "varanasi", "nagpur",
  "indore", "kanpur", "nashik", "faridabad"
];

const SLEEP_OPTIONS = [
  "5-6 hours", "Less than 5 hours", "7-8 hours", "More than 8 hours", "Others"
];

const DIET_OPTIONS = ["Healthy", "Moderate", "Unhealthy", "Others"];

const DEGREE_OPTIONS = [
  "Class 12", "B.Ed", "B.Com", "B.Arch", "BCA", "MSc", "B.Tech", "MCA",
  "M.Tech", "BHM", "BSc", "M.Ed", "B.Pharm", "M.Com", "BBA", "MBBS",
  "LLB", "BE", "BA", "M.Pharm", "MD", "MBA", "MA", "PhD", "LLM", "MHM",
  "ME", "Others"
];

function fillSelect(id, options) {
  const select = document.getElementById(id);
  select.innerHTML = options
    .map((opt) => `<option value="${opt}">${opt}</option>`)
    .join("");
}

fillSelect("city", CITY_OPTIONS);
fillSelect("sleep_duration", SLEEP_OPTIONS);
fillSelect("dietary_habits", DIET_OPTIONS);
fillSelect("degree", DEGREE_OPTIONS);

const form = document.getElementById("predictForm");
const resultBox = document.getElementById("result");
const jsonOutput = document.getElementById("jsonOutput");
const submitBtn = document.getElementById("submitBtn");

function showResult(text, className) {
  resultBox.textContent = text;
  resultBox.className = `result ${className}`;
}

function showJson(data) {
  jsonOutput.textContent = JSON.stringify(data, null, 2);
  jsonOutput.classList.remove("hidden");
}

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const apiUrl = document.getElementById("apiUrl").value.replace(/\/+$/, "");

  const payload = {
    gender: document.getElementById("gender").value,
    age: Number(document.getElementById("age").value),
    city: document.getElementById("city").value,
    academic_pressure: Number(document.getElementById("academic_pressure").value),
    cgpa: Number(document.getElementById("cgpa").value),
    study_satisfaction: Number(document.getElementById("study_satisfaction").value),
    sleep_duration: document.getElementById("sleep_duration").value,
    dietary_habits: document.getElementById("dietary_habits").value,
    degree: document.getElementById("degree").value,
    suicidal_thoughts: document.getElementById("suicidal_thoughts").value,
    work_study_hours: Number(document.getElementById("work_study_hours").value),
    financial_stress: Number(document.getElementById("financial_stress").value),
    family_history_of_mental_illeness: document.getElementById("family_history_of_mental_illeness").value
  };

  submitBtn.disabled = true;
  submitBtn.textContent = "Predicting...";
  resultBox.classList.add("hidden");
  jsonOutput.classList.add("hidden");

  try {
    const response = await fetch(`${apiUrl}/predict`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload)
    });

    const data = await response.json();

    if (data.Error) {
      showResult(`Error: ${data.Error}`, "error");
    } else {
      const isYes = data.Depressed === "Yes";
      showResult(
        isYes ? "Prediction: Depressed - Yes" : "Prediction: Depressed - No",
        isYes ? "yes" : "no"
      );
    }

    showJson(data);
  } catch (err) {
    showResult(`Request failed: ${err.message}. Check the API URL and CORS settings.`, "error");
  } finally {
    submitBtn.disabled = false;
    submitBtn.textContent = "Predict";
    resultBox.classList.remove("hidden");
  }
});
