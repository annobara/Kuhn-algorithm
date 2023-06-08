from flask import flash


def parse_form(request):

    if request.form['left'].isdigit() and request.form['right'].isdigit() and request.files['file'].filename == "":
        leftVertex = int(request.form['left'])
        rightVertex = int(request.form['right'])
        matrix = request.form['text'].splitlines()

    elif request.files['file'].filename != "":
        try:
            file = request.files['file'].read().decode().split('\n')
            if (file[0]==''):
                flash('Файл не может быть пустым')
                return
            leftVertex = int(file[0].split(' ')[0])
            rightVertex = int(file[0].split(' ')[1])
            matrix = file[1:]
        except:
            flash('Ошибка прочтения файла. Убедитесь, что файл загружен в нужном формате')
            return
        
    else:
        flash('Введите данные')
        return 
    
    if leftVertex<1 or rightVertex<1:
        flash("Количество вершин не может быть меньше одного")
        return

    if (leftVertex < len(matrix)):
        flash("Длина списка смежности не может быть больше количества вершин. Лишние строки будут проигнорированы")
    edges = [[]]*leftVertex
    for i in range (min(leftVertex, len(matrix))):
        if matrix[i]=='':
            continue
        try:
            for x in matrix[i].split(' '):
                j = int(x)
                if j<0 or j>rightVertex:
                    raise ValueError
            edges[i] = [int(x) for x in matrix[i].split(' ')]
        except:
            flash('Некорректный тип данных в поле ввода. Список смежности должен быть заполнен целыми числами, которые соответсвтуют индексам вершин')
            return
           
    return edges, leftVertex, rightVertex