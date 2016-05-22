WORK_EXPERIENCE = [
    {
        'title': 'Freelancers Union',
        'address': 'Brooklyn, NY',
        'dates': 'July 2015 - present',
        'role': 'Full Stack Developer',
        'skills': 'python, django, rest-framework, psql, angular.js, jquery.js, xml/svg',
        'bullets': [
            'build robust and scalable web applications for organization with +350k members',
            'jira project tracking with trello integration. strictly defined git workflow.',
            'collaboration with graphic designers and qa for refined ux design',
            'focused on backend technologies (data- and application layers)',
            "lead development for organization's central revenue generation: online health insurance sales experience",
        ]
    },
    {
        'title': 'Aptitude Analytics',
        'address': 'Middletown, NJ',
        'dates': 'March 2015 - present',
        'role': 'Lead Developer (Consultant)',
        'skills': 'python, django, psql, nginx, uwsgi, aws',
        'bullets': [
            'reverse-engineered legacy algorithm for hr consulting platform',
            'built new processing architecture as cloud-based web-service (hosted on ec2)',
            'focused on lean, scalable code in favor of making alterations to the algorithm',
            'following unix philosophy, personally insisted on shipping a fully-refactored 2. generation of codebase',
        ]
    },
    {
        'title': 'Great Believers',
        'address': 'Brooklyn, NY',
        'dates': 'January 2016 - present',
        'role': 'Full Stack Developer (part-time)',
        'skills': 'php, wordpress, apache, linux, aws, xml/svg',
        'bullets': [
            'develop and host wordpress sites for clients of non-profit organization',
            'receive design specifications to develop WP themes and plugins from scratch',
            'migrate and maintain mySQL databases from existing projects and production environments',
        ]
    },
    {
        'title': 'Rukkus, Inc.',
        'address': 'Manhattan, NY',
        'dates': 'January 2015 - March 2015',
        'role': 'Backend Developer',
        'skills': 'python, django, rest-framework, psql, backbone.js',
        'bullets': [
            'develop backend technologies to support event ticket sales platform',
            'focus on scalable API systems for iOS and Android app data services',
            'developed testing suite for code base for improved work flow and development',
            'startup culture, worked long hours with high-pressure on fast product delivery',
        ]
    },
]

PROGRAMMING = [
    {
        'title': 'Backend',
        'lines': [
            'python (django, rest-framework, celery, cms, itertools, numpy), rabbitmq',
            'php (wordpress), moderately proficient in c++, java, clojure, rust'
        ]
    },
    {
        'title': 'Frontend',
        'lines': [
            'javascript (angular, backbone, jquery, grunt',
            'HTML5, Less/CSS3, bootstrap3, XML (svg)'
        ]
    },
    {
        'title': 'Database',
        'lines': [
            'postgreSQL, mySQL, redis, mongo',
        ]
    },
    {
        'title': 'Deployment',
        'lines': [
            'linux (os), nginx, apache, aws/ami, heroku, vagrant',
        ]
    }
]


CAREER_GOAL = {
    'goal': ''.join(('Advance my expertise in developing robust, scalable web applications. ',
                     'I wish to always improve my technical abilities ',
                     'follow best practices for more performant, maintainable code.'))
}

EDUCATION = [
    {
        'title': 'Byte Academy',
        'location': 'New York, NY',
        'completion_date': 'December 2014',
        'description': ''.join(('12-week intensive coding boot camp teaching full-stack programming. ',
                                'Focus on python, OO and financial services.'))
    },
    {
        'title': 'Johns Hopkins University',
        'location': 'Baltimore, MD',
        'completion_date': 'May 2012',
        'description': ''.join(('Bachelor of Arts, dual major in ',
                                '<strong>Neuroscience</strong> and ',
                                '<strong>Philosophy</strong>. GPA 3.6'))
    }
]

CONTACT = {
    'street': '11 Jones St #12',
    'city_state': 'New York, NY 10014',
    'email': 'lbrambrink@gmail.com',
    'phone': '503 490 2573',
}

LUCAS_BRAMBRINK = {
    'name': 'Lucas Brambrink',
    'contact': CONTACT,
    'career_goal': CAREER_GOAL,
    'education': EDUCATION,
    'programming': PROGRAMMING,
    'experience': WORK_EXPERIENCE
}


FONTS = (
    ('Lato-Thin, Lato-ThinItalic, Arial, sans-serif;', 'Lato-Thin'),
    ('Helvetica, Arial, sans-serif;', 'Helvetica'),
    ('Georgia, Arial, sans-serif', 'Georgia')
)
