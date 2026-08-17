// HireCraft - Career Analysis Form

const careerForm = document.getElementById("career-analysis-form");

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

    // Display collected data
    console.log("HireCraft Career Profile:");
    console.log(careerProfile);

    // Send data to FastAPI backend
    const response = await fetch("http://127.0.0.1:8000/api/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(careerProfile)
    });

    // Get backend response
    const data = await response.json();

    // Display backend response
    console.log("Backend Response:", data);
});