import graphviz

# Создание графа
graph = graphviz.Digraph(format='png', engine='dot', node_attr={'shape': 'box'})

# Добавление элементов процесса
graph.node('start', 'Начало', shape='ellipse')
graph.node('submit_request', 'Подача заявки', shape='rectangle')
graph.node('check_request', 'Проверка заявки', shape='rectangle')
graph.node('compare_offers', 'Сравнительный анализ', shape='rectangle')
graph.node('select_contractor', 'Выбор подрядчика', shape='diamond')
graph.node('sign_contract', 'Подписание договора', shape='rectangle')
graph.node('execute_work', 'Выполнение услуг', shape='rectangle')
graph.node('check_work', 'Проверка выполненных работ', shape='rectangle')
graph.node('acceptance', 'Приемка работ', shape='rectangle')
graph.node('payment', 'Оплата подрядчику', shape='rectangle')
graph.node('end', 'Завершение', shape='ellipse')

# Добавление связей между элементами
graph.edge('start', 'submit_request')
graph.edge('submit_request', 'check_request')
graph.edge('check_request', 'compare_offers')
graph.edge('compare_offers', 'select_contractor')
graph.edge('select_contractor', 'sign_contract', label='Выбор\nподрядчика')
graph.edge('sign_contract', 'execute_work')
graph.edge('execute_work', 'check_work')
graph.edge('check_work', 'acceptance')
graph.edge('acceptance', 'payment')
graph.edge('payment', 'end')

# Сохранение диаграммы в файл
graph.format = 'png'
graph.render('business_process', cleanup=True, format='png', directory='C:\II')

print("Диаграмма создана успешно.")
