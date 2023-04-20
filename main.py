
from GrupoComtribuinte import GrupoDeContribuintes
from pessoaFisica import PessoaFisica
from pessoaJuridica import PessoaJuridica


p1 = PessoaFisica('Kezia', '121.321.456-10', 2600, 'Feminino')
p2 = PessoaFisica('Roberta', '123.654.321-13', 3660, 'Feminino')
p3 = PessoaJuridica('Empresa XX', '01.234.567/0001-89', 18000, 2020)
p4 = PessoaFisica('Renato', '321.805.123-45', 1800, 'Masculinho')
p5 = PessoaFisica('Carlos', '482.862.369-20', 3100,'Masculino')


grupo = GrupoDeContribuintes()
grupo.addContribuinte(p1)
grupo.addContribuinte(p2)
grupo.addContribuinte(p3)
grupo.addContribuinte(p4)
grupo.addContribuinte(p5)


print('Total de imposto devido: R$' + str(grupo.getTotalImposto()))


print('Porcentagem de contribuintes do sexo feminino:' + str(grupo.getPorcentagemContribuintesFeminino()))
