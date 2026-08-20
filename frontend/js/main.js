// HireCraft - Career Analysis Form

const careerForm = document.getElementById("career-analysis-form");

const analysisResult = document.getElementById("analysis-result");
const matchPercentage = document.getElementById("match-percentage");
const matchedSkills = document.getElementById("matched-skills");
const skillGaps = document.getElementById("skill-gaps");
const recommendations = document.getElementById("recommendations");


careerForm.addEventListener("submit", async function (event) {

    // Prevent normal form submission
    event.preventDefault();

    // Get form values
    const formData = new FormData(careerForm);

    // Create career profile object
    const careerProfile = {
        full_name: formData.get("full_name"),
        current_role: formData.get("current_role"),
        skills: formData.get("skills"),
        experience: formData.get("experience"),
        projects: formData.get("projects"),
        education: formData.get("education"),
        target_job_description: formData.get("job_description")
    };

    // Display collected data in console
    console.log("HireCraft Career Profile:");
    console.log(careerProfile);


    try {

        // Send data to FastAPI backend
        const response = await fetch(
            "http://127.0.0.1:8000/api/analyze",
            {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify(careerProfile)
            }
        );


        // Check HTTP status
        if (!response.ok) {
            throw new Error(`API request failed: ${response.status}`);
        }


        // Get backend response
        const data = await response.json();


        console.log("Backend Response:", data);


        // Get analysis data
        const analysis = data.data.analysis;

        document.getElementById("match-percentage").textContent =
            `${analysis.match_percentage}%`;

        document.getElementById("matched-skills").innerHTML =
            analysis.matched_skills
                .map(skill => `<li>${skill}</li>`)
                .join("");

        document.getElementById("skill-gaps").innerHTML =
            analysis.skill_gaps
                .map(gap => `<li>${gap.skill} — ${gap.priority} priority</li>`)
                .join("");

        document.getElementById("recommendations").innerHTML =
            analysis.recommendations
                .map(recommendation => `<li>${recommendation}</li>`)
                .join("");

        document.getElementById("analysis-result").style.display = "block";


        // Display match percentage
        matchPercentage.textContent =
            `${analysis.match_percentage}%`;


        // Clear previous results
        matchedSkills.innerHTML = "";
        skillGaps.innerHTML = "";
        recommendations.innerHTML = "";


        // Display matched skills
        analysis.matched_skills.forEach(function (skill) {

            const li = document.createElement("li");

            li.textContent = skill;

            matchedSkills.appendChild(li);
        });


        // Display skill gaps
        analysis.skill_gaps.forEach(function (gap) {

            const li = document.createElement("li");

            li.textContent =
                `${gap.skill} — ${gap.priority} priority`;

            skillGaps.appendChild(li);
        });


        // Display recommendations
        analysis.recommendations.forEach(function (recommendation) {

            const li = document.createElement("li");

            li.textContent = recommendation;

            recommendations.appendChild(li);
        });


        // Show analysis result section
        analysisResult.hidden = false;


    } catch (error) {

        console.error("HireCraft API Error:", error);

        alert(
            "Unable to analyze your career profile. " +
            "Please make sure the HireCraft backend is running."
        );
    }

});