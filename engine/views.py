from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import CreateUserForm


from django.http import JsonResponse
from django.core import serializers

memory = 0
import time


class MyTimer:
    def __init__(self, min):
        self.sec_left = time.time()
        self.start_time = time.time()
        self.finish_time = self.start_time + min * 60

    def sec_to_finish(self):
        if self.finish_time > time.time():
            self.sec_left = int(self.finish_time - time.time())
        return self.sec_left

timer = MyTimer(90)



def create_user(request):
    if request.user.is_authenticated:
        return redirect('intro1')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                new_user = authenticate(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                )
                login(request, new_user);

                user = form.cleaned_data.get('username')
                messages.success(request, f'Account was created for {user}.')
                return redirect('login')

        ctx = {'form': form}
        return render(request, 'engine/registration.html', ctx)


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
    return render(request, 'engine/loging.html', ctx)


def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def start_page(request):
    global timer 
    timer = MyTimer(90)
    ctx = {
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
            'next_btn': reverse('check_mutations')
        }
    if page == 'tbl_video':
        ctx = {
            'video': 'virus_table',
            'back_btn': reverse('table'),
        }
    if page == 'suites_video':
        ctx = {
            'video': 'suites',
            'back_btn': reverse('suites'),
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
def picture(request, page):
    global timer
    # ctx = {'time': timer.sec_to_finish()}
    ctx = dict()
    if page == 'microscope':
        ctx.update({
            'picture': '/static/engine/images/microscope.jpg',
            'btn_1': reverse('microscope_v'),
            'btn_1_label': 'Watch video',
            'btn_2': reverse('microscope_look'),
            'btn_2_label': ' Watch',
            'btn_3': reverse('check_microscope'),
            'btn_3_label': ' Watch with loupe',
            'btn_back': reverse('laboratory'),
        })
    if page == 'microscope_look':
        ctx.update({
            'picture': '/static/engine/images/microscope_look.jpg',
            'btn_back': reverse('microscope'),
        })
    if page == 'small_table':
        ctx.update({
            'picture': '/static/engine/images/small_table.jpg',
            'btn_2': reverse('check_probes'),
            'btn_2_label': ' Probes',
            'btn_3': reverse('small_table_v'),
            'btn_3_label': 'Watch video',
            'btn_back': reverse('laboratory'),
        })
    if page == 'reagents':
        ctx.update({
            'picture': '/static/engine/images/reagent.jpg',
            'btn_2': reverse('probes'),
            'btn_2_label': ' Probes',
            'btn_back': reverse('laboratory'),
        })
    if page == 'suites':
        ctx.update({
            'btn_2': reverse('suites_v'),
            'btn_2_label': 'Watch video',
            'btn_3': reverse('suites_p'),
            'btn_3_label': 'See picture',
            'picture': '/static/engine/images/him.jpg',
            'btn_back': reverse('laboratory'),
        })
    if page == 'tv':
        ctx.update({
            'picture': '/static/engine/images/tv.jpg',
            'btn_2': reverse('tv_v1'),
            'btn_2_label': ' Watch video about Animals',
            'btn_3': reverse('check_mutations'),
            'btn_3_label': 'Watch video about Mutations',
            'btn_back': reverse('laboratory'),
        })
    if page == 'table':
        ctx.update({
            'picture': '/static/engine/images/table.jpg',
            'btn_1': reverse('table_s'),
            'btn_1_label': 'Symptoms',
            'btn_2': reverse('table_p'),
            'btn_2_label': 'Check table',
            'btn_3': reverse('table_v'),
            'btn_3_label': 'Watch video',
            'btn_4': reverse('table_n'),
            'btn_4_label': 'Watch news',
            'btn_back': reverse('laboratory'),
        })
    if page == 'paper':
        ctx.update({
            'picture': '/static/engine/images/paper.jpg',
            'btn_back': reverse('table'),
        })
    if page == 'door':
        ctx.update({
            'picture': '/static/engine/images/door.jpg',
            'btn_1': reverse('room3'),
            'btn_1_label': 'Left panel',
            'btn_2': reverse('room2'),
            'btn_2_label': 'Right panel',
            'btn_back': reverse('laboratory'),
        })
    return render(request, 'engine/page_static.html', ctx)

@login_required(login_url='login')
def puzzle(request, page):
    if page == 'probes':
        ctx = {
            'picture': '/static/engine/images/probirki.jpg',
            'ans_1': True,
            'ans_2': True,
            'ans_3': True,
            'ans_4': True,
            'btn_back': reverse('small_table'),
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

def quest_room_2(request):
    return render(request, 'engine/room_1.html', {})

def quest_room_3(request):
    ans = request.POST.get('answer')
    ctx = {
        'picture': '/static/engine/images/cell.jpg',
    }
    answers = {
        'ABAEFGCDHLKJIMNOP',
        'ABAEFIJMNOKGCDHLP',
        'AEABCDHGFJIMNOKLP',
        'ABAEIMNJFGCDHLKOP',
        'ABAEIMNOKJFGCDHLP',
        'AEABFJIMNOKGCDHLP',
        'AEABFJIMNOKGCDHLP',
        'AEABFJCDHLKJIMNOP'
    }
    print(ans)
    if ans is not None:
        if ans.upper() in answers:
            answer = """
                   Enter in 3 room
            """
            ctx = {
                'text': answer,
                'video': 'blur'
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_room3.html', ctx)
    else:
        return render(request, 'engine/quest_room3.html', ctx)


@login_required(login_url='login')
def quest_news(request):
    ctx = {'hint_1': "There are 5 correct facts and 7 wrong"}
    ans = request.POST.get('answer')
    if ans is not None:
        if ans.lower() == 'plague':
            answer = """
            The purple vaccine should
            but below the blue,
            and not next to it
            """
            ctx = {
                'text': answer,
                'video': 'blur',
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_news.html', ctx)
    else:
        return render(request, 'engine/quest_news.html', ctx)

def quest_microscope(request):
    print(request)
    ans = request.POST.get('ans')
    ctx = {'hint_1': "There are 5 letters in one of the pictures. Find them an make a word."}
   
    print(ans)
    if ans is not None:
        if ans == 'EBOLA':
            answer = """
            The place for the white vaccine is directly above the orange one
            """
            ctx = {
                'text': answer,
                'video': 'blur',
                'btn_back': reverse('microscope'),
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_microscope.html', ctx)
    else:
        return render(request, 'engine/quest_microscope.html', ctx)


@login_required(login_url='login')
def quest_symptoms(request):
    ctx = {}
    ans = request.POST.get('ans')
    if ans is not None:
        if ans == '28':
            answer = """
            the Yellow above green
            """
            ctx = {
                'text': answer,
                'video': 'blur'
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_symptoms.html', ctx)
    else:
        ctx = {
            'video': 'symptoms',
            'hint_1': "10000/10= 1000. 1000/5= 200. 200/2=100. 100/4=25. 25/5=5. 5/5=0. Totally you’ve made 31 tests. But there can be less.",
        }
        return render(request, 'engine/quest_symptoms.html', ctx)


@login_required(login_url='login')
def quest_mutations(request):
    ctx = {
        'video': 'tv_mutations',
        'hint_1': " С + G = CG",
    }
    ans1 = request.POST.get('ans1')
    ans2 = request.POST.get('ans2')
    ans3 = request.POST.get('ans3')
    ans4 = request.POST.get('ans4')
    print(ans1, ans2, ans3, ans4)
    if ans1 is not None and ans2 is not None and ans3 is not None and ans4 is not None :
        if ans1 == 'GH' and ans2 == 'DA' and ans3 == 'EB' and ans4 == 'CF':
            answer = """
            The yellow vaccine should be next to red
            """
            ctx = {
                'text': answer,
                'video': 'blur'
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_mutations.html', ctx)
    else:
        return render(request, 'engine/quest_mutations.html', ctx)


@login_required(login_url='login')
def quest_probs(request):
    ctx = {
        'picture': '/static/engine/images/probirki.jpg',
        'hint_1': "You need to find a hint with color mixing.",
    }
    ans1 = request.POST.get('ans1')
    ans2 = request.POST.get('ans2')
    ans3 = request.POST.get('ans3')
    ans4 = request.POST.get('ans4')
    print(ans1, ans2, ans3, ans4)
    if ans1 is not None and ans2 is not None and ans3 is not None and ans4 is not None :
        if ans1.upper() == 'EBOLA' and ans2.upper() == 'MERS' and ans3.upper() == 'FLU' and ans4.upper() == 'CORONA':
            answer = """
            The purple vaccine should be above the green but not next to it
            """
            ctx = {
                'text': answer,
                'video': 'blur'
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_probes.html', ctx)
    else:
        return render(request, 'engine/quest_probes.html', ctx)

@login_required(login_url='login')
def quest_cell(request):
    ans = request.POST.get('ans')
    ctx = {
        'picture': '/static/engine/images/cell.jpg',
        'hint_1': "Test hint",
    }
    print(ans)
    if ans is not None:
        if ans == '7':
            answer = """
                   but below the blue, and not next to it.
            """
            ctx = {
                'text': answer,
                'video': 'blur'
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_cell.html', ctx)
    else:
        return render(request, 'engine/quest_cell.html', ctx)

@login_required(login_url='login')
def quest_suites(request):
    ctx = {'hint_1': "Test hint"}
    glasses = request.POST.get('glasses')
    masks = request.POST.get('masks')
    gloves = request.POST.get('gloves')
    print(glasses, masks, gloves)
    if glasses is not None:
        if glasses == '2' and masks == '5' and gloves == '4':
            answer = """
            4 other vaccines should
            be above the red one
            """
            ctx = {
                'text': answer,
                'video': 'blur'
            }
            return render(request, 'engine/page_show_tips.html', ctx)
        else:
            return render(request, 'engine/quest_picture.html', ctx)
    else:
        return render(request, 'engine/quest_picture.html', ctx)


@login_required(login_url='login')
def lab_probes(request):
    ctx = {'picture': '/static/engine/images/probirki.jpg'}
    return render(request, 'engine/pazzle_probes.html', ctx)







@login_required(login_url='login')
def lab_reagents(request):
    ctx = {'picture': '/static/engine/images/reagenty.jpg'}
    return render(request, 'engine/lab_reagents.html', ctx)


