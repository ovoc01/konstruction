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
    <%@include file="../include/style.jsp" %>
    <title>Ecole</title>
</head>
<body>
<div class="layout-wrapper layout-content-navbar">
    <div class="layout-container">

        <%@include file="../include/sidebar.jsp" %>
        <div class="layout-page">

            <div class="content-wrapper">
                <div class="container-xxl flex-grow-1 container-p-y">
                    <div class="row">

                        <div class="col-md-6 col-lg-8 mb-3">
                            <div class="card">

                                <div class="card-body">
                                    <h5 class="card-title">Remettre la base donnée à 0</h5>
                                    <a href="/extra/resetdb" class="btn btn-primary">Réinitialiser</a>
                                </div>
                            </div>
                            <%
                                if (request.getParameter("message") != null) { %>
                                    <div class="alert mt-3 alert-success alert-dismissible" role="alert">
                                        <%=request.getParameter("message")%>
                                        <button type="button" class="btn-close" data-bs-dismiss="alert"
                                        aria-label="Close"></button>
                            </div>
                            <% }%>
                            <%
                                if (request.getParameter("error") != null) { %>
                                <div class="alert mt-3 alert-danger alert-dismissible" role="alert">
                                <%=request.getParameter("error") %>
                                <button type="button" class="btn-close" data-bs-dismiss="alert"
                                        aria-label="Close"></button>
                                </div>
                           <% } %>

                        </div>

                    </div>

                </div>
                <div class="content-backdrop fade"></div>
            </div>
            <!-- Content wrapper -->
        </div>

    </div>

</div>


<%@include file="../include/script.jsp" %>
</body>
</html>