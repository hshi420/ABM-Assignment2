import mesa


class PDAgent(mesa.Agent):
    """Agent member of the iterated, spatial prisoner's dilemma model."""

    def __init__(self, pos, model, starting_move=None):
        """
        Create a new Prisoner's Dilemma agent.

        Args:
            pos: (x, y) tuple of the agent's position.
            model: model instance
            starting_move: If provided, determines the agent's initial state:
                           C(ooperating) or D(efecting). Otherwise, random.
        """
        super().__init__(pos, model)
        self.pos = pos
        self.score = 0
        if starting_move:
            self.move = starting_move
        else:
            self.move = self.random.choice(["C", "D"])
        self.next_move = None

    @property
    def isCooroperating(self):
        return self.move == "C"

    def step(self):
        """Get the best neighbor's move, and change own move accordingly if better than own score."""
        neighbors = self.model.grid.get_neighbors(self.pos, True, include_center=False)
 
        moves = [neighbor.move for neighbor in neighbors]
        print(moves)


        C_score = sum(self.model.payoff[('C', move)] for move in moves if move is not None)
        D_score = sum(self.model.payoff[('D', move)] for move in moves if move is not None)
        
        if C_score > D_score:
            self.next_move = 'C'
        else:
            self.next_move = 'D'

        if self.model.schedule_type != "Simultaneous":
            self.advance()

    def advance(self):
        self.move = self.next_move
#       self.score += self.increment_score()

'''
    def increment_score(self):
        neighbors = self.model.grid.get_neighbors(self.pos, True)
        if self.model.schedule_type == "Simultaneous":
            moves = [neighbor.next_move for neighbor in neighbors]
        else:
            moves = [neighbor.move for neighbor in neighbors]
        return sum(self.model.payoff[(self.move, move)] for move in moves)
'''
