from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm


def create_user(request):
    if request.user.is_authenticated:
        return redirect('intro1')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}.')
                return redirect('login')

        ctx = {'form': form}
        return render(request, 'engine/register.html', ctx)


def login_user(request):
    if request.user.is_authenticated:
        return redirect('start')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('start')
        else:
            messages.info(request, 'Username or password incorrect')

    ctx = {}
    return render(request, 'engine/login.html', ctx)


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def start_page(request):
    start_text = \
    """
    You have a chance to investigate a mystery from the past:
    the year 2020, an opening of the time capsule solemnly buried in
    2000 turns into a worldwide mystery when strange files named
    SARS-CoV-2 are discovered among its contents.

    Now is the time to gather your thoughts and call friends (zoom, facetime, etc)
    Before you start, be sure to read the rules of the game.
    """
    ctx = {
        'start_text': start_text,
        'video': 'blur',
        'btn_show': False,
    }
    return render(request, 'engine/start.html', ctx)



@login_required(login_url='login')
def video(request, page):
    if page == 'start':
        ctx = {
            'video': 'intro',
            'next_btn': reverse('intro1'),
        }
    if page == 'intro1':
        ctx = {
            'video': 'intro',
            'next_btn': reverse('intro2'),
        }
    if page == 'intro2':
        ctx = {
            'video': 'intro_at',
            'back_btn': reverse('intro1'),
            'next_btn': reverse('laboratory')
        }
    if page == 'tv_animals':
        ctx = {
            'video': 'tv_animals',
            'back_btn': reverse('tv'),
        }
    if page == 'tv_mutations':
        ctx = {
            'video': 'tv_mutations',
            'back_btn': reverse('tv'),
            'next_btn': reverse('tv_puzzle')
        }
    if page == 'tbl_video':
        ctx = {
            'video': 'virus_table',
            'back_btn': reverse('table'),
        }
    if page == 'small_tbl_video':
        ctx = {
            'video': 'human_cell',
            'back_btn': reverse('small_table'),
            'next_btn': reverse('check_cell')
        }
    if page == 'microscope_video':
        ctx = {
            'video': 'microscope',
            'back_btn': reverse('microscope'),
        }
    return render(request, 'engine/page_video.html', ctx)

@login_required(login_url='login')
def static(request, page):
    if page == 'microscope':
        ctx = {
            'picture': '/static/engine/images/microscope.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Lavoratory',
            'btn_2': reverse('microscope_look'),
            'btn_2_label': ' Watch',
            'btn_3': reverse('check_microscope'),
            'btn_3_label': 'Watch with lens',
            'btn_4': reverse('microscope_v'),
            'btn_4_label': 'Watch video',
        }
    if page == 'microscope_look':
        ctx = {
            'picture': '/static/engine/images/microscope_look.jpg',
            'btn_1': reverse('microscope'),
            'btn_1_label': 'Microscope',
        }
    if page == 'small_table':
        ctx = {
            'picture': '/static/engine/images/small_table.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Laboratory',
            'btn_2': reverse('probes'),
            'btn_2_label': ' Probes',
            'btn_3': reverse('small_table_v'),
            'btn_3_label': 'Watch video',
        }
    if page == 'reagents':
        ctx = {
            'picture': '/static/engine/images/reagenty.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Laboratory',
            'btn_2': reverse('probes'),
            'btn_2_label': ' Probes',
        }
    if page == 'suites':
        ctx = {
            'picture': '/static/engine/images/him.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Laboratory',
        }
    if page == 'tv':
        ctx = {
            'picture': '/static/engine/images/tv.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Laboratory',
            'btn_2': reverse('tv_v1'),
            'btn_2_label': ' Watch video about Animals',
            'btn_3': reverse('tv_v2'),
            'btn_3_label': 'Watch video about Mutations',
        }
    if page == 'table':
        ctx = {
            'picture': '/static/engine/images/table.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Laboratory',
            'btn_2': reverse('table_p'),
            'btn_2_label': 'Check paper',
            'btn_3': reverse('table_v'),
            'btn_3_label': 'Watch video',
            'btn_4': reverse('table_n'),
            'btn_4_label': 'Watch news',
        }
    if page == 'paper':
        ctx = {
            'picture': '/static/engine/images/paper.jpg',
            'btn_1': reverse('laboratory'),
            'btn_1_label': 'Laboratory',
            'btn_2': reverse('table'),
            'btn_2_label': 'Table',
        }
    return render(request, 'engine/page_static.html', ctx)

@login_required(login_url='login')
def puzzle(request, page):
    if page == 'probes':
        ctx = {
            'picture': '/static/engine/images/probirki.jpg',
            'btn_1': reverse('small_table'),
            'btn_1_label': 'Table',
            'btn_2': reverse('reagents'),
            'btn_2_label': 'Reagents',
            'ans_1': True,
            'ans_2': True,
            'ans_3': True,
            'ans_4': True,
        }
    return render(request, 'engine/page_puzzle.html', ctx)

@login_required(login_url='login')
def check_answers(request, page):
    ans_1 = request.POST.get('ans_1')
    ans_2 = request.POST.get('ans_2')
    ans_3 = request.POST.get('ans_3')
    ans_4 = request.POST.get('ans_4')
    print(ans_1, ans_2, ans_3, ans_4)
    cor_ans_1, cor_ans_2, cor_ans_3, cor_ans_4 = '', '', '', ''
    print(page)
    if page == 'probes':
        puz = {
            'ans_1': 'EBOLA',
            'ans_2': 'MERS',
            'ans_3': 'FLU',
            'ans_4': 'CORONA',
            'ans_text': "The purple vaccine should be above the green but not next to it."
        }
    if ans_1: 
        if ans_1.upper() == puz['ans_1']:
            cor_ans_1 = ans_1
    if ans_2: 
        if ans_2.upper() == puz['ans_2']:
            cor_ans_2 = ans_2
    if ans_3: 
        if ans_3.upper() == puz['ans_3']:
            cor_ans_3 = ans_3
    if ans_4: 
        if ans_4.upper() == puz['ans_4']:
            cor_ans_4 = ans_4
    if all([cor_ans_1, cor_ans_2, cor_ans_3, cor_ans_4]):
        ctx = {
            'text': puz['ans_text'],
            'video': 'blur'
        }
        return render(request, 'engine/page_solve.html', ctx)
    else:
        ctx = {
            'answ_1': cor_ans_1, 
            'answ_2': cor_ans_2, 
            'answ_3': cor_ans_3, 
            'answ_4': cor_ans_4, 
            'picture': '/static/engine/images/probirki.jpg',
            'btn_1': reverse('small_table'),
            'btn_1_label': 'Table',
            'btn_2': reverse('reagents'),
            'btn_2_label': 'Reagents',
            'ans_1': True,
            'ans_2': True,
            'ans_3': True,
            'ans_4': True,
        }
        return render(request, 'engine/page_puzzle.html', ctx)

@login_required(login_url='login')
def room_1(request):
    return render(request, 'engine/room_1.html', {})


@login_required(login_url='login')
def lab_table_news(request):
    ctx = {'picture': '/static/engine/images/news_page.jpg'}
    return render(request, 'engine/lab_tab_news.html', ctx)


@login_required(login_url='login')
def lab_table_news_check(request, answer='text text'):
    print(request)
    ans = request.GET.get('answer')
    print(ans)
    if ans.lower() == 'plague':
        answer = """
        The purple vaccine should
        but below the blue,
        and not next to it
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tab_news_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/news_page.jpg'}
        return render(request, 'engine/lab_tab_news.html', ctx)




@login_required(login_url='login')
def lab_tv_puzzle(request):
    print(request)
    ans1 = request.GET.get('ans1')
    ans2 = request.GET.get('ans2')
    ans3 = request.GET.get('ans3')
    ans4 = request.GET.get('ans4')
    print(ans1, ans2, ans3, ans4)
    if ans1 == 'GH' and ans2 == 'DA' and ans3 == 'EB' and ans4 == 'CF':
        answer = """
        The yellow vaccine should be next to red
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tv_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/mutation.jpg'}
        return render(request, 'engine/lab_tv_puzzle.html', ctx)


@login_required(login_url='login')
def lab_probes(request):
    ctx = {'picture': '/static/engine/images/probirki.jpg'}
    return render(request, 'engine/pazzle_probes.html', ctx)


@login_required(login_url='login')
def lab_probes_check(request):
    print(request)
    ans1 = request.GET.get('ans1')
    ans2 = request.GET.get('ans2')
    ans3 = request.GET.get('ans3')
    ans4 = request.GET.get('ans4')
    print(ans1, ans2, ans3, ans4)
    if ans1.upper() == 'EBOLA' and ans2.upper() == 'MERS' and ans3.upper() == 'FLU' and ans4.upper() == 'CORONA':
        answer = """
        The purple vaccine should be above the green but not next to it
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tab_news_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/probirki.jpg'}
        return render(request, 'engine/pazzle_probes.html', ctx)

@login_required(login_url='login')
def microscope_check(request):
    print(request)
    ans1 = request.GET.get('ans1')
   
    print(ans1)
    if ans1 == 'EBOLA':
        answer = """
        The place for the white vaccine is directly above the orange one
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tab_news_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/microscope_look_loupe.jpg'}
        return render(request, 'engine/pazzle_microscope.html', ctx)

@login_required(login_url='login')
def cell_check(request):
    print(request)
    ans1 = request.GET.get('ans1')
    print(ans1)
    if ans1 == '7':
        answer = """
        but below the blue,
        and not next to it
        """
        ctx = {
            'text': answer,
            'video': 'blur'
        }
        return render(request, 'engine/lab_tv_solve.html', ctx)
    else:
        ctx = {'picture': '/static/engine/images/cell.jpg'}
        return render(request, 'engine/pazzle_cell.html', ctx)

@login_required(login_url='login')
def lab_reagents(request):
    ctx = {'picture': '/static/engine/images/reagenty.jpg'}
    return render(request, 'engine/lab_reagents.html', ctx)


@login_required(login_url='login')
def room_1_2d(request):
    ctx = {'picture': '/static/engine/images/lab.jpg'}
    return render(request, 'engine/laboratory.html', ctx)

