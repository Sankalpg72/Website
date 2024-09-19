from flask import Flask, render_template

app = Flask(__name__)
About = "Lorem ipsum odor amet, consectetuer adipiscing elit. Consectetur aenean egestas mi consectetur; sapien orci nam porttitor. Donec efficitur turpis, eget nisl nulla senectus quisque metus. Cursus habitant ultricies laoreet mollis maecenas. Class scelerisque cubilia iaculis facilisi habitant ornare enim. Mollis pulvinar efficitur ullamcorper duis praesent ut mauris. Facilisi nam purus ornare; aenean quis vulputate. Ex egestas orci venenatis egestas aptent felis. Neque maecenas vitae tincidunt eros parturient turpis eget magna elementum. Rhoncus felis varius; penatibus ante eleifend donec condimentum. Rhoncus habitant congue luctus tortor sollicitudin ligula felis purus. Vulputate consequat eros aenean sodales diam volutpat. Sagittis ornare purus; natoque nisl sociosqu pretium mattis eleifend. Malesuada libero non varius praesent platea. Nunc lorem dui cras neque mauris tincidunt. Varius vestibulum commodo erat est dis. Dis class accumsan inceptos accumsan dapibus. Mi eget velit, imperdiet sed nec metus taciti id. Ornare natoque pharetra praesent mi inceptos sapien vitae pharetra. Inceptos convallis nisi pharetra, quisque integer nascetur est. Habitant hendrerit fringilla ornare ultricies fames etiam suspendisse molestie enim. Maximus commodo dolor ad massa maecenas cubilia velit. Curae integer tristique nec proin venenatis cursus facilisis. In curabitur taciti accumsan torquent felis vulputate. Sem porttitor sagittis lacus ex urna curae rhoncus. Dapibus ultrices luctus in per tempus praesent dis. Massa vulputate pretium id condimentum habitant magnis. Volutpat senectus vulputate praesent suscipit massa elementum felis aliquet torquent. Tristique pellentesque fusce habitasse, euismod tempor amet nunc consequat. Sollicitudin imperdiet dignissim magna inceptos eros placerat etiam. Primis porta integer netus erat lectus parturient diam cras eros. Magna vivamus morbi feugiat quam donec sociosqu magna. Suspendisse purus primis pulvinar posuere quisque turpis. Felis magnis lobortis sed rhoncus himenaeos ad mauris. Dis netus primis odio dolor orci. Volutpat consequat phasellus quis; etiam proin dapibus potenti senectus. Orci nec iaculis facilisis nullam odio molestie? Vehicula proin netus ante vestibulum neque lectus curabitur. Penatibus nam netus viverra non proin habitant quisque. Vitae pulvinar dolor dui, nullam justo vestibulum sollicitudin gravida. Massa curabitur montes quis nisi tortor. Vivamus orci faucibus diam suscipit tempor curabitur platea venenatis. Sociosqu dui enim etiam egestas nec ante ut. Ante enim nisl integer facilisi taciti phasellus ridiculus quis. Consectetur curae netus nostra habitasse ultricies laoreet. Eleifend ac mattis suscipit maximus viverra vel suspendisse habitasse. Mi massa egestas at sagittis euismod. Purus vitae nascetur molestie; aptent tempus ligula. Massa sed phasellus turpis maecenas eleifend nibh est diam. Ad justo bibendum; accumsan consectetur ultricies maximus. Ligula vulputate semper risus pulvinar dui potenti venenatis maximus. Quam viverra quis fermentum dapibus luctus vehicula mauris. Ornare suspendisse natoque maecenas suscipit, hendrerit praesent? Metus non eget taciti eget nunc luctus."
@app.route("/")
def hello_world():
    return render_template('Bootstrap.html', about=About)

@app.route('/gene')
def gene():
    return render_template('gene.html')

@app.route('/Genome')
def Genome():
    return render_template('Genome.html')
    
if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug = True)

#In Flask, the default convention for locating HTML templates is to look in a folder named templates. This is built into Flask's template rendering system. Here’s why using template instead of templates didn’t work:

# Flask Convention: Flask expects the directory where templates are stored to be named templates. This is a convention followed by the Flask framework. If the directory name is different, Flask won’t be able to locate the templates.

