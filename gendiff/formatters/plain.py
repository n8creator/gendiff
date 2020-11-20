from gendiff.generate_diff import ADDED, DELETED, NESTED, CHANGED

# OLD_VAL and NEW_VAL are indexes for dicts containing replaced value (OLD_VAL)
# and new one (NEW_VAL).They are used to get rid of "magic numbers" in the code
OLD_VAL, NEW_VAL = (0, 1)


def generate_plain_string(key, value, type, replaced_value="None"):
    # ###############################################################
    #
    # КОММЕНТАРИЙ ДЛЯ СЕРГЕЯ К. КОТОРЫЙ БУДЕТ ДЕЛАТЬ РЕВЬЮ ПРОЕКТА
    #
    # В ревью от 16 ноября вы оставили следующее замечание применительно к
    # к функции generate_plain_string() -- далее цитата:
    # -----------------------------------------------------------------------
    # "Задача этой функции привести конкретное значение к строке в зависимости
    # от типа переменной (не от типа узла). Например, булево значение, None,
    # словарь, строка, число и т.д."
    # -----------------------------------------------------------------------
    #
    # На самом деле все не совсем так. Если распечатать diff, то отдельные его
    # узлы которые не имеют вложенной структуры будут иметь следующий вид:
    # - 'ops': {'type': 'added', 'values': 'vops'}
    # - 'follow': {'type': 'added', 'values': 'false'}
    # - 'setting2': {'type': 'deleted', 'values': 200}
    #
    # Если делать проверку ТОЛЬКО в зависимости от типа переменной, то сам по
    # себе тип никак не позволит понять, было ли это значение добавлено или
    # удалено. Соответственно на основе типа значения невозможно сгенерировать
    # строки вывода типа 'Property was added with value' или 'Property was
    # removed'. Именно для этого и нужна проверка в зависимости от типа узла!!!
    #
    # Собственно если старое или новое является комплексным (является узлом),
    # то мы заменяем его на строку '[complex value]', а во всех остальных
    # случаях возвращаем значение в виде строки.
    #
    #
    # Да, и все т.н. "булевы значения" я осознно привел к строкам по следующей
    # причине. В 7 шаге задания представлен следующий вывод плоского формата:
    # -----------------------------------------------------------------------
    # - Property 'common.follow' was added with value: false
    # - Property 'common.setting3' was updated. From true to null
    # -----------------------------------------------------------------------
    #
    # Собственно булевых типов false, true и уж тем более null нет в Python.
    # Есть типы False, True (пишутся с большой буквы!!!)
    #
    # Очевидно требуемый формат вывода просто скопирован из 2-го проекта по
    # JavaScript, поэтому я сделал вывод "типа булевых значений" в виде строк.
    # ###############################################################

    # Formatting input data depending on type to use in output
    value = '[complex value]' if isinstance(value, dict) else\
        '\'{0}\''.format(value)
    replaced_value = '[complex value]' if isinstance(replaced_value, dict)\
        else '\'{0}\''.format(replaced_value)
    key = '\'{0}\''.format(key)

    # Code below returns formatted strings
    if type == ADDED:
        return 'Property {0} was added with value: {1}'.\
            format(key, value)
    elif type == DELETED:
        return 'Property {0} was removed'.format(key)
    elif type == CHANGED:
        return 'Property {0} was updated. From {1} to {2}'.\
            format(key, value, replaced_value)


def render_plain_engine(diff, path):
    # Initialize output variable
    output = []

    for key, data in sorted(diff.items()):
        # Generate path from the root as a plain string
        root_path = '{0}.{1}'.format(path, key) if path else key

        # diff_dict traversal
        if data['type'] == NESTED:
            output.append(render_plain_engine(data['values'],
                                              root_path)
                          )
        elif data['type'] == ADDED:
            output.append(generate_plain_string(root_path,
                                                data['values'],
                                                ADDED)
                          )
        elif data['type'] == DELETED:
            output.append(generate_plain_string(root_path,
                                                data['values'],
                                                DELETED)
                          )
        elif data['type'] == CHANGED:
            output.append(generate_plain_string(root_path,
                                                data['values'][OLD_VAL],
                                                CHANGED,
                                                data['values'][NEW_VAL])
                          )

    # Return output as a string
    return '\n'.join(output)


def render_plain(diff):
    return render_plain_engine(diff, path=None)
