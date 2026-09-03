# HireCraft - LinkedIn Profile Optimization Service

from app.schemas.linkedin_profile import LinkedInProfileOptimization


# Generate LinkedIn Profile Optimization

def generate_profile_optimization(
    target_role: str,
    required_skills: list[str],
) -> LinkedInProfileOptimization:
    """
    Generate LinkedIn profile optimization recommendations
    using only the target role and required skills.

    No existing LinkedIn profile information is required.
    """

    target_role = target_role.strip()

    skills = [
        skill.strip()
        for skill in required_skills
        if skill and skill.strip()
    ]

    # Remove duplicates while preserving order
    skills = list(dict.fromkeys(skills))

    # 1. Headline Variants

    headline_variants = []

    if skills:

        skill_text = " | ".join(skills[:3])

        headline_variants = [
            f"{target_role} | {skill_text} | Open to Opportunities",

            f"Aspiring {target_role} | "
            f"{skill_text} | Building Practical Projects",

            f"{target_role} | "
            f"Software Development | {skill_text}",
        ]

    else:

        headline_variants = [
            f"{target_role} | Open to Opportunities",

            f"Aspiring {target_role} | Building Practical Projects",

            f"{target_role} | Software Development",
        ]


    # 2. About Section Structure

    about_structure = [
        f"Start with a clear introduction focused on {target_role}.",
        "Mention the technical skills relevant to the target role.",
        "Describe practical learning, development and project-building activities.",
        "Explain the type of opportunities being targeted.",
        "End with a clear professional growth and career direction statement.",
    ]


    # 3. Keyword Strategy

    keyword_strategy = [
        f"Use the target role '{target_role}' naturally across the profile.",
        "Include relevant technical skills in the About section.",
        "Use important skills in project descriptions where applicable.",
        "Use consistent terminology between the profile and job searches.",
        "Avoid keyword stuffing and keep profile content readable.",
    ]


    # 4. Priority Skills

    priority_skills = skills[:10]


    # 5. Featured Section Strategy

    featured_section_strategy = [
        "Feature the strongest target-role-relevant project.",
        "Add project demonstrations or technical documentation when available.",
        "Highlight GitHub repositories related to the target role.",
        "Prioritize projects that demonstrate the required technical skills.",
    ]


    # 6. Project Visibility Strategy

    project_visibility_strategy = [
        f"Prioritize projects demonstrating skills relevant to {target_role}.",
        "Use clear project titles that communicate the technical purpose.",
        "Mention the technologies used in each project.",
        "Explain the problem solved and the implementation approach.",
        "Link relevant projects to GitHub when available.",
    ]


    # 7. Profile Keyword Map

    profile_keyword_map = {
        "target_role": [
            target_role
        ],

        "technical_skills": skills,

        "profile_sections": [
            "Headline",
            "About",
            "Skills",
            "Projects",
            "Featured",
        ],
    }


    # 8. Return Structured Result

    return LinkedInProfileOptimization(
        headline_variants=headline_variants,
        about_structure=about_structure,
        keyword_strategy=keyword_strategy,
        priority_skills=priority_skills,
        featured_section_strategy=featured_section_strategy,
        project_visibility_strategy=project_visibility_strategy,
        profile_keyword_map=profile_keyword_map,
    )