from flask import request
from wtforms import Form
from app.libs.error_code import ParameterException



class BaseForm(Form):
    def __init__(self):
        data = request.get_json(silent=True)        # 获取request.json数据; 静默: body为空的话不报错 -> 不用request.json()
        args = request.args.to_dict()
        super(BaseForm, self).__init__(data=data, **args)

    def validate_for_api(self):
        valid = super(BaseForm, self).validate()
        if not valid:
            # 错误都存在form.errors
            raise ParameterException(msg=self.errors)
        return self     # 返回form
