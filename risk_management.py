class RiskManagement:
    def __init__(self, account_balance, risk_percentage):
        self.account_balance = account_balance
        self.risk_percentage = risk_percentage

    def calculate_position_size(self, stop_loss_distance):
        risk_amount = self.account_balance * (self.risk_percentage / 100)
        position_size = risk_amount / stop_loss_distance
        return position_size

    def update_account_balance(self, profit_or_loss):
        self.account_balance += profit_or_loss
        return self.account_balance

# Example usage:
if __name__ == '__main__':
    risk_management = RiskManagement(account_balance=10000, risk_percentage=2)
    position_size = risk_management.calculate_position_size(stop_loss_distance=50)
    print(f'Position Size: {position_size}')