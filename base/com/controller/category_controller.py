from flask import render_template, request, redirect
from base import app
from base.com.vo.category_vo import CategoryVO
from base.com.dao.category_dao import CategoryDAO


@app.route('/')
def admin_homepage():
    try:
        return render_template("/admin/homePage.html")
    except Exception as exception:
        print("admin_homepage error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)

@app.route('/admin/load_category')
def load_category():
    try:
        return render_template("/admin/addCategory.html")
    except Exception as exception:
        print("admin_homepage error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)

@app.route('/admin/insert_category', methods=["post"])
def admin_insert_category():
    try:
        category_name = request.form.get("categoryName")
        category_description = request.form.get("categoryDescription")

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.insert_category(category_vo)
        return redirect("/")
    except Exception as exception:
        print("admin_insert_category error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)



@app.route('/admin/view_category')
def admin_view_category():
    try:
        category_dao = CategoryDAO()
        category_vo_list = category_dao.view_category()
        return render_template("/admin/viewCategory.html", category_vo_list=category_vo_list)
    except Exception as exception:
        print("admin_view_category error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)
    
@app.route('/admin/delete_category', methods=["get"])
def admin_delete_category():
    try:
        category_id = request.args.get("categoryId")

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        print(category_vo)
        category_dao.delete_category(category_vo)
        return redirect("/admin/view_category")
    except Exception as exception:
        print("admin_delete_category error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)

@app.route('/admin/edit_category', methods=["get"])
def admin_edit_category():
    try:
        category_id = request.args.get("categoryId")

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        category_vo_list = category_dao.edit_category(category_vo)
        return render_template("admin/updateCategory.html", category_vo_list=category_vo_list)
    except Exception as exception:
        print("admin_edit_category error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)

@app.route('/admin/update_category', methods=["post"])
def admin_update_category():
    try:
        category_name = request.form.get("categoryName")
        category_description = request.form.get("categoryDescription")
        category_id = request.form.get("categoryID")

        category_vo = CategoryVO()
        category_dao = CategoryDAO()

        category_vo.category_id = category_id
        category_vo.category_name = category_name
        category_vo.category_description = category_description

        category_dao.update_category(category_vo)
        return redirect("/admin/view_category")
    except Exception as exception:
        print("admin_update_category error>>>>>", exception)
        return render_template("/admin/viewError.html", exception=exception)