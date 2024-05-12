<mvc:resources mapping="/resources/**" location="/resources/static/"/>
<%@ page pageEncoding="UTF-8" contentType="text/html; charset=UTF-8" %>


<!doctype html>

<html lang="en">
<head>
    <base href="http://localhost:8080/">
    <meta charset="UTF-8">
    <meta name="viewport"
          content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <%@include file="include/style.jsp" %>
    <title>Ecole</title>
</head>
<body>
<div class="layout-wrapper layout-content-navbar">
    <div class="layout-container">

        <%@include file="include/sidebar.jsp" %>
        <div class="layout-page">
            <!-- Navbar -->


            <!-- / Navbar -->

            <!-- Content wrapper -->
            <div class="content-wrapper">
                <div class="container-xxl flex-grow-1 container-p-y">
                    

                </div>

                <div class="content-backdrop fade"></div>
            </div>
            <!-- Content wrapper -->
        </div>

    </div>

</div>


<%@include file="include/script.jsp" %>
</body>
</html>