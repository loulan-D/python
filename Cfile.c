/*
用c实现一个简单的ATM机系统
复习goto/break/continue/if/while/
用到do-while循环
首先输入用户名和密码
正在读卡--显示界面
1，查看账户信息，假设原先有1000元
2，存款纸币面额为100元
3，取款纸币面额为100元
4，跨行转账收取手续费
5，所有操作完成，1，是发送短信接收回执单2.通过打印回执单
6.退卡
7.谢谢本次光临，为本次服务做出评价，是否？
谢谢
*/
#include <stdio.h>
#include <stdlib.h>
int main()
{
    char name[30],feedback;
    int pass,num,num1,num2,num3,money,rmb=1000;
    printf("程序：一个简单的小程序\n");
    printf("版本：version1\n");
    printf("作者：loulan\n");
    printf("日期：2017/04/17\n");
    printf("语言：C语言\n");
    printf("操作：用户根据提示输入相关的内容\n");
    printf("功能：实现一个简单的ATM机系统\n");
    do{
        printf("\t\t\t\t欢迎光临******银行\t\t\t\t\n");
        printf("请输入用户名:\n");
        scanf("%s",name);
        printf("请输入密码：\n");
        scanf("%d",&pass);
        printf("USERNAME:%s\t\nPASSWORD:******\n",name);
        printf("---------------------\n");
        printf("正在读卡，请稍等..............\n");

        up: {printf("1:查看账户信息\t2:存款\t3:取款\t4:跨行转账 5:退卡\n");
            scanf("%d",&num);
            switch(num)
            {
            case 1:
                printf("您的账户信息为：\n");
                printf("用户名：%s\n开户日期：2017/04/17\n开户银行:中国****银行河北分行\n账户余额：%dRMB\n",name,rmb);
                printf("---------------------\n");
                printf("按5退卡\t按0返回上一层\n");
                scanf("%d",&num1);
                if (num1 == 0)
                    goto up;
                else
                    goto end;
                break;
            case 2:
                printf("请输入你的存款金额:\n");
                scanf("%d",&money);
                printf("你当前的账户余额为:%d\n",rmb += money);
                printf("---------------------\n");
                printf("按5退卡\t按0返回上一层\n");
                scanf("%d",&num1);
                if (num1 == 0)
                    goto up;
                else
                    goto end;
                break;
            case 3:
                printf("请输入您的取款金额:\n");
                scanf("%d",&money);
                printf("你当前的账户余额为:%d\n",rmb -= money);
                printf("---------------------\n");
                printf("按5退卡\t按0返回上一层\n");
                scanf("%d",&num1);
                if (num1 == 0)
                    goto up;
                else
                    goto end;
                break;
            case 4:
                printf("---------------------\n");
                printf("请注意跨行转账会收取相应的手续费:\n");
                printf("请选择你需要转入的银行：\n");
                printf("1:建设银行\t2：人民银行\t3：工商银行\n");
                scanf("%d",&num3);
                switch(num3)
                {
                case 1:
                    printf("请输入你要转取的金额\n");
                    scanf("%d",&money);
                    printf("您当前的账户余额为%d\n",rmb -= money);
                    printf("按5退卡\t按0返回上一层\n");
                    scanf("%d",&num1);
                    if (num1 == 0)
                        goto up;
                    else
                        goto end;
                    break;
                case 2:
                    printf("请输入你要转取的金额\n");
                    scanf("%d",&money);
                    printf("您当前的账户余额为%d\n",rmb -= money);
                    printf("按5退卡\t按0返回上一层\n");
                    scanf("%d",&num1);
                    if (num1 == 0)
                        goto up;
                    else
                        goto end;
                    break;
                case 3:
                    printf("请输入你要转取的金额\n");
                    scanf("%d",&money);
                    printf("您当前的账户余额为%d\n",rmb -= money);
                    printf("按5退卡\t按0返回上一层\n");
                    scanf("%d",&num1);
                    if (num1 == 0)
                        goto up;
                    else
                        goto end;
                    break;
                }
                break;

                    }
        }

        end :{
            printf("是否为本次服务评价？y/n\n");
            scanf(" %c",&feedback);
            if (feedback == 'y')
                {printf("按5满意\t按4良好\t按3一般\t按2差\n");
                scanf("%d",&num2);
                switch(num2)
                {
                case 5:
                    printf("谢谢光临，欢迎下次再来！\n");
                    break;
                case 4:
                    printf("嗯，好吧..主人您不太满意哦，下次我会好好工作的，相信我，主人，下次见哟！\n");
                    break;
                case 3:
                    printf("嗯？怎么搞的？不要这样的啦，主人，人家今天没有吃饱饭，不要怪罪人家的嘛！下次见哦主人！\n");
                    break;
                case 2:
                    printf("哎？今天又没有好好工作，我的工资又飞了，不过没关系，下次我会好好努力的，主人，再见！\n");
                break;
                default:
                    printf("谢谢光临，欢迎下次再来！\n");
                    break;
                }
                }

            else
                printf("谢谢光临，欢迎下次再来！\n");
        }

    }while(1);

    return 0;
}
