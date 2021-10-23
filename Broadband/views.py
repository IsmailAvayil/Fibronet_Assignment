from django.shortcuts import render
from.models import Login,Customer_Reg,Worker_Reg,Plans_Reg,Admin_Request,Customer_complaints
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'home.html')
def login_in(request):
    return render(request,'login_in.html')
def Login_Res(request):
    try:
        m = Login.objects.get(User_Name=request.POST['user'],Password=request.POST['pswd'],Account=request.POST['type'])
        if m.status ==1:
            request.session['user'] = m.User_Name
            return render(request, 'Admin_page.html')

        if m.status ==3:
            request.session['user'] = m.User_Name
            user=request.POST['user']
            data =Worker_Reg.objects.filter(User_Name=user)
            return render(request,'Lineworker_page.html',{'line':data})
        if m.status ==2:
            request.session['user'] = m.User_Name
            user=request.POST['user']
            data=Customer_Reg.objects.filter(User_Name=user)
            return render(request, 'Customer_page.html',{'cus':data})

        else:
            return render(request,'login_in.html',{'error':" Your username & password didn't match"})
    except:
        return render(request,'login_in.html',{'error':"Your username didn't match."})
def  Logout_Window(request):
        A=request.session['user']
        try:
            del request.session['user']
        except keyError:
            pass
        return render(request,'login_in.html',{'na':A})
def add_customers(request):
    plns=Plans_Reg.objects.all()
    return render(request,'add_customers.html',{'plans':plns})
def cus_reg_submit(request):
    Customer_type=request.POST['cus_type']
    postpaid=request.POST['postpaid']
    plan = request.POST['plan']
    reg_id = request.POST['reg_id']
    reg_date=request.POST['reg_date']
    date_of_birth=request.POST['date_of_birth']
    full_name=request.POST['full_name']
    address = request.POST['address']
    email=request.POST['email']
    mobile_no = request.POST['mobile_no']
    user_name = request.POST['user_name']
    password = request.POST['password']
    house_no = request.POST['house_no']
    village=request.POST['village']
    city=request.POST['city']
    state=request.POST['state']
    district=request.POST['district']
    main_locality=request.POST['main_locality']
    data=Customer_Reg(Customer_type=Customer_type,Pre_Postpaid_type =postpaid,Applied_plan=plan,Register_ID =reg_id, Registration_date = reg_date, Date_of_Birth = date_of_birth,Full_Name = full_name, Address = address,  Email=email,Mobile_no =mobile_no,User_Name=user_name,H_no = house_no,Village_Colony=village,District =district,City=city,State=state,Main_Locality =main_locality,)
    data.save()
    dete=Login(User_Name=user_name,Password=password,Account='Customer',status=2)
    dete.save()
    return render(request,'Admin_page.html')

def customer_view(request):
    id = request.POST['id']
    data=Customer_Reg.objects.filter(id=id)
    return render(request,'customer_view.html',{'cus':data})
def customer_delete(request):
    id = request.POST['id']
    Customer_Reg.objects.filter(id=id).delete()
    return render(request,'customers_details.html')
def customers_details(request):
    data=Customer_Reg.objects.all()
    return render(request,'customers_details.html',{'cus':data})
def add_lineworkers(request):
    return render(request,'add_lineworkers.html')
def line_reg_submit(request):
    lineworker_id=request.POST['lineworker_id']
    full_name = request.POST['full_name']
    age = request.POST['age']
    address = request.POST['address']
    email = request.POST['email']
    mobile_no = request.POST['mobile_no']
    user_name = request.POST['user_name']
    password = request.POST['password']
    det=Worker_Reg(Lineworker_ID =lineworker_id,Full_Name =full_name, Age =age ,Address =address,Email =email,Mobile_no =mobile_no)
    det.save()
    dete=Login(User_Name=user_name,Password=password,Account='Lineworker',status=3)
    dete.save()
    return render(request,'Admin_page.html')

def lineworkers_details(request):
    det=Worker_Reg.objects.all()
    return render(request,'lineworkers_details.html',{'line':det})
def add_newplans(request):
    return render(request,'add_newplans.html')
def update_plans(request):
    return render(request,'update_plans.html')
def Password_window(request):
    return render(request,'Password_window.html')
def customer_contact(request):

    return render(request,'customer_contact.html')

def admin_plan_reg(request):
    return render(request, 'admin_plan_reg.html')
def admin_plan_res(request):
    pln1=request.POST['pln1']
    plndet1=request.POST['plndet1']
    pln2=request.POST['pln2']
    plndet2=request.POST['plndet2']
    pln3=request.POST['pln3']
    plndet3=request.POST['plndet3']
    pln4=request.POST['pln4']
    plndet4=request.POST['plndet4']
    pln5=request.POST['pln5']
    plndet5=request.POST['plndet5']
    pln6=request.POST['pln6']
    plndet6=request.POST['plndet6']
    pln7=request.POST['pln7']
    plndet7=request.POST['plndet7']
    Plans=Plans_Reg(Plan1=pln1, Plan1_Det=plndet1, Plan2=pln2,Plan2_Det =plndet2,Plan3 =pln3, Plan3_Det =plndet3, Plan4 =pln4, Plan4_Det =plndet4,Plan5=pln5,Plan5_Det =plndet5, Plan6=pln6,Plan6_Det =plndet6,Plan7=pln7,Plan7_Det =plndet7)
    Plans.save()
    return render(request,'Admin_page.html')
def admin_plan_view(request):
    plns=Plans_Reg.objects.all()
    return render(request,'admin_plan_view.html',{'plans':plns})
def admin_plan_update(request):
    plns=Plans_Reg.objects.all()
    return render(request,'admin_plan_update.html',{'plans':plns})
def admin_plan_updated_res(request):
    id=request.POST['id']
    pln1=request.POST['pln1']
    plndet1=request.POST['plndet1']
    pln2=request.POST['pln2']
    plndet2=request.POST['plndet2']
    pln3=request.POST['pln3']
    plndet3=request.POST['plndet3']
    pln4=request.POST['pln4']
    plndet4=request.POST['plndet4']
    pln5=request.POST['pln5']
    plndet5=request.POST['plndet5']
    pln6=request.POST['pln6']
    plndet6=request.POST['plndet6']
    pln7=request.POST['pln7']
    plndet7=request.POST['plndet7']
    Plans_Reg.objects.filter(id=id).update(Plan1=pln1, Plan1_Det=plndet1, Plan2=pln2,Plan2_Det =plndet2,Plan3 =pln3, Plan3_Det =plndet3, Plan4 =pln4, Plan4_Det =plndet4,Plan5=pln5,Plan5_Det =plndet5, Plan6=pln6,Plan6_Det =plndet6,Plan7=pln7,Plan7_Det =plndet7)
    plns=Plans_Reg.objects.all()
    return render(request,'admin_plan_view.html',{'plans':plns})

def customer_profile(request):
    id = request.POST['id']
    data = Customer_Reg.objects.filter(id=id)
    return render(request,'customer_profile.html',{'cus':data})
def worker_profile(request):
    id = request.POST['id']
    data = Worker_Reg.objects.filter(id=id)
    return render(request,'worker_profile.html',{'line':data})
def Dashboard(request):
    return render(request,'Dashboard.html')
def Admin_page(request):
    return render(request,'Admin_page.html')
def Admin_oldpswd(request):
    id=request.POST['id']
    old=request.POST['oldpswd']
    pswd2=request.POST['pswd2']
    try:
        m=Login.objects.get(User_Name=request.session['user'],Password=request.POST['old'],Account=request.POST['type'])
        if m.status == 1:
            Login.objects.filter(User_Name=request.session['user']).update( Password=pswd2)
            return render(request, 'Admin_page.html')
        else:
            return render(request, 'Password_window.html',{'cmt':"oldpswd not matching"})
    except:
        return render(request,'login_in.html',{'error':"Your username didn't match."})


def request_form(request):
    return render(request, 'request_form.html')

def requst_res(request):
    register_id=request.POST['register_id']
    reg=Customer_Reg.objects.filter(Register_ID=register_id)
    return render(request,'request_form.html',{'cus':reg})

def request_submit(request):
    txt=request.POST['txt']
    id=request.POST['id']
    reg = Customer_Reg.objects.filter(id=id)
    for i in reg:
        ret=Admin_Request(Customer_type=i.Customer_type,Applied_plan=i.Applied_plan,Full_Name =i.Full_Name, Address =i.Address,Mobile_no = i.Mobile_no,H_no = i.H_no,Village_Colony= i.Village_Colony,City=i.City,Main_Locality =i.Main_Locality,Customer_Complaint=txt)
        ret.save()
    return render(request, 'Admin_page.html')

def worker_inbox(request):
    Inb=Admin_Request.objects.all()
    return render(request,'worker_inbox.html',{'Abt':Inb})
def customer_inform(request):
    return render(request,'customer_inform.html')
def inform_submit(request):
    try:
         m= Customer_Reg.objects.get(Register_ID=request.POST['reg_id'],Full_Name=request.POST['full_name'])
         if True:
             reg_id = request.POST['reg_id']
             full_name = request.POST['full_name']
             subject = request.POST['subject']
             message = request.POST['message']
             data=Customer_complaints(Registered_id=reg_id,Full_Name=full_name,Subject=subject,Message=message)
             data.save()
             return render(request,'Customer_page.html')
         else:
            return render(request,'customer_inform.html',{'error': "register id or full name is not matching "})
    except:
         return render(request, 'customer_inform.html', {'na': "the person is not registered here!"})



def complaints(request):
    data=Customer_complaints.objects.all()
    return render(request,'compaints.html',{'cpm':data})
def worker_plan_view(request):
    plns=Plans_Reg.objects.all()
    return render(request,'worker_plan_view.html',{'plans':plns})
def lineworker_page(reuest):
    return render(reuest,'Lineworker_page.html')
def customer_plan_view(request):
    plns=Plans_Reg.objects.all()
    return render(request, 'customer_plan_view.html', {'plans': plns})
def Customer_page(reuest):
    return render(reuest,'Customer_page.html')
def About(request):
    return render(request,'About.html')

