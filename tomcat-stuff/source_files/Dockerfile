FROM tomcat
LABEL maintainer="@elmofiedboby"
COPY tomcat-users.xml /usr/local/tomcat/conf
RUN cp -r /usr/local/tomcat/webapps.dist/ROOT /usr/local/tomcat/webapps
RUN cp -r /usr/local/tomcat/webapps.dist/host-manager /usr/local/tomcat/webapps
RUN cp -r /usr/local/tomcat/webapps.dist/manager /usr/local/tomcat/webapps
RUN cp -r /usr/local/tomcat/webapps.dist/docs /usr/local/tomcat/webapps
COPY context.xml /usr/local/tomcat/webapps/host-manager/META-INF
COPY context.xml /usr/local/tomcat/webapps/manager/META-INF
