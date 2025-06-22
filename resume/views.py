from django.shortcuts import render, redirect

# === Personal Information ===
def personal_info(request):
    if request.method == 'POST':
        request.session['personal_info'] = {
            'full_name': request.POST.get('full_name', ''),
            'profession': request.POST.get('profession', ''),
            'phone': request.POST.get('phone', ''),
            'email': request.POST.get('email', ''),
            'country': request.POST.get('country', ''),
            'city': request.POST.get('city', ''),
            'linkedin': request.POST.get('linkedin', ''),
            'github': request.POST.get('github', ''),
            'portfolio': request.POST.get('portfolio', ''),
            'twitter': request.POST.get('twitter', ''),
            'address': request.POST.get('address', ''),
            'summary': request.POST.get('summary', ''),
        }
        return redirect('education')
    return render(request, 'personal_info.html')


# === Education Details ===
def education(request):
    if request.method == 'POST':
        education_count = int(request.POST.get('education_count', 1))
        education_data = []

        for i in range(1, education_count + 1):
            education_data.append({
                'institution': request.POST.get(f'institution_{i}', ''),
                'degree': request.POST.get(f'degree_{i}', ''),
                'field': request.POST.get(f'field_{i}', ''),
                'start_date': request.POST.get(f'start_date_{i}', ''),
                'end_date': request.POST.get(f'end_date_{i}', ''),
                'description': request.POST.get(f'description_{i}', '')
            })

        request.session['education_data'] = education_data
        return redirect('skills')
    return render(request, 'education.html')


# === Skills ===
def skills(request):
    if request.method == 'POST':
        skill_count = int(request.POST.get('skill_count', 1))
        skills_data = []

        for i in range(1, skill_count + 1):
            skills_data.append({
                'name': request.POST.get(f'skill_name_{i}', ''),
                'description': request.POST.get(f'skill_desc_{i}', '')
            })

        request.session['skills_data'] = skills_data
        return redirect('experience')
    return render(request, 'skills.html')


# === Work Experience ===
def experience(request):
    if request.method == 'POST':
        experience_count = int(request.POST.get('experience_count', 1))
        experience_data = []

        for i in range(1, experience_count + 1):
            experience_data.append({
                'company': request.POST.get(f'company_{i}', ''),
                'position': request.POST.get(f'position_{i}', ''),
                'start_date': request.POST.get(f'start_date_{i}', ''),
                'end_date': request.POST.get(f'end_date_{i}', ''),
                'current': request.POST.get(f'current_{i}', 'off') == 'on',
                'description': request.POST.get(f'description_{i}', '')
            })

        request.session['experience_data'] = experience_data
        return redirect('projects')
    return render(request, 'experience.html')


# === Projects ===
def projects(request):
    if request.method == 'POST':
        if request.POST.get('skip') == 'true':
            request.session['projects_data'] = []
            return redirect('additional_details')

        project_count = int(request.POST.get('project_count', 1))
        projects_data = []

        for i in range(1, project_count + 1):
            projects_data.append({
                'name': request.POST.get(f'project_name_{i}', ''),
                'technologies': request.POST.get(f'technologies_{i}', '').split(','),
                'description': request.POST.get(f'project_desc_{i}', ''),
                'link': request.POST.get(f'project_link_{i}', '')
            })

        request.session['projects_data'] = projects_data
        return redirect('additional_details')
    return render(request, 'projects.html')


# === Additional Details ===
def additional_details(request):
    if request.method == 'POST':
        if request.POST.get('skip') == 'true':
            request.session['additional_data'] = {
                'certifications': [],
                'achievements': [],
                'volunteer_work': [],
                'hobbies': ''
            }
            return redirect('resume')

        # Certifications
        cert_count = int(request.POST.get('cert_count', 1))
        certifications = [
            {
                'name': request.POST.get(f'cert_name_{i}', ''),
                'organization': request.POST.get(f'cert_org_{i}', ''),
                'issue_date': request.POST.get(f'cert_date_{i}', ''),
                'expiry_date': request.POST.get(f'cert_expiry_{i}', ''),
                'link': request.POST.get(f'cert_link_{i}', '')
            }
            for i in range(1, cert_count + 1)
        ]

        # Achievements
        achievement_count = int(request.POST.get('achievement_count', 1))
        achievements = [
            {
                'title': request.POST.get(f'achievement_name_{i}', ''),
                'organization': request.POST.get(f'achievement_org_{i}', ''),
                'date': request.POST.get(f'achievement_date_{i}', ''),
                'description': request.POST.get(f'achievement_desc_{i}', '')
            }
            for i in range(1, achievement_count + 1)
        ]

        # Volunteer Work
        volunteer_count = int(request.POST.get('volunteer_count', 1))
        volunteer_work = [
            {
                'organization': request.POST.get(f'volunteer_org_{i}', ''),
                'role': request.POST.get(f'volunteer_role_{i}', ''),
                'start_date': request.POST.get(f'volunteer_start_{i}', ''),
                'end_date': request.POST.get(f'volunteer_end_{i}', ''),
                'description': request.POST.get(f'volunteer_desc_{i}', '')
            }
            for i in range(1, volunteer_count + 1)
        ]

        # Hobbies
        hobbies = request.POST.get('hobbies', '')

        request.session['additional_data'] = {
            'certifications': certifications,
            'achievements': achievements,
            'volunteer_work': volunteer_work,
            'hobbies': hobbies
        }

        return redirect('resume')
    return render(request, 'additional_details.html')


# === Final Resume View ===
def resume(request):
    context = {
        'personal_info': request.session.get('personal_info', {}),
        'education_data': request.session.get('education_data', []),
        'skills_data': request.session.get('skills_data', []),
        'experience_data': request.session.get('experience_data', []),
        'projects_data': request.session.get('projects_data', []),
        'additional_data': request.session.get('additional_data', {})
    }
    return render(request, 'resume.html', context)
